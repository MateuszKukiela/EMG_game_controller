from obci_cpp_amplifiers.amplifiers import TmsiCppAmplifier, DummyCppAmplifier
import numpy as np
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller
import scipy.signal as ss
import numpy as np
from scipy.signal import butter, buttord  # funkcje do projektowania filtrów
from scipy.signal import lfilter, filtfilt  # funkcje do aplikowania filtrów
import time
from MDM.MDM import MDM, Base
from obci_readmanager.signal_processing.smart_tags_manager import SmartTagsManager
from obci_readmanager.signal_processing.tags.smart_tag_definition import (
    SmartTagDurationDefinition,
    SmartTagEndTagDefinition,
)
from obci_readmanager.signal_processing.read_manager import ReadManager
from scipy.signal import butter, filtfilt
import matplotlib.pyplot as plt

number_of_players = 2
player1_start = 0
player1_stop = 6
player2_start = 7
player2_stop = 12
channels = 3
path_player1 = "player_data/gracz1"
path_player2 = "player_data/gracz1"
mouse = Controller()
keyboard = Controller()


def click():
    mouse.press(Button.left)
    mouse.release(Button.left)


def button_up():
    keyboard.press(Key.up)
    time.sleep(0.05)
    keyboard.release(Key.up)


def button_down():
    keyboard.press(Key.down)
    time.sleep(0.05)
    keyboard.release(Key.down)


def button_w():
    keyboard.press("w")
    time.sleep(0.05)
    keyboard.release("w")


def przycisks():
    keyboard.press("s")
    time.sleep(0.05)
    keyboard.release("s")


train_data_players = []

# Creating ReadManager object
for path in (path_player1, path_player2):
    mgr = ReadManager(f"{path}.xml", f"{path}.raw", f"{path}.tag")

    # Informacje o sygnale
    Fs = float(mgr.get_param("sampling_frequency"))
    num_channels = int(mgr.get_param("number_of_channels"))
    print(num_channels)
    channel_names = mgr.get_param("channels_names")
    gestureDuration = 1  # in seconds

    # Gestures
    gestures = ["gora", "dol", "piesc"]
    gestureID = np.arange(len(gestures))

    # length of signal snipet
    num_samples = int(gestureDuration * Fs)

    # number of samples in each gesture
    tags = mgr.get_tags()
    tag_cnt = {}
    for i in mgr.iter_tags():
        k = i["name"]
        tag_cnt[k] = int(tag_cnt[k]) + 1 if k in tag_cnt.keys() else 1
    gestureSample = max(tag_cnt.values())

    # filters parameters:
    b, a = butter(5, (25 / (Fs / 2), 160 / (Fs / 2)), btype="bandpass")
    # b,a = butter(5, 10/(Fs/2), btype = 'highpass')
    # d,c = butter(1, np.array([49,51])/(Fs/2), btype = 'bandstop')

    # Array to store cut data:
    trainData = np.zeros(
        (len(gestureID), gestureSample, int(num_channels / 2), num_samples)
    )
    tmpTrainData = np.zeros((len(gestureID), gestureSample, num_channels, num_samples))
    raw = tmpTrainData.copy()
    # cutting and filters:
    for j in gestureID:
        k = 0  # Array filling counter
        # Cutting parameters
        tag_def = SmartTagDurationDefinition(
            start_tag_name=gestures[j],
            start_offset=0.0,
            end_offset=0.0,
            duration=gestureDuration,
        )
        smgr = SmartTagsManager(tag_def, f"{path}.xml", f"{path}.raw", f"{path}.tag")
        for i_smart_tag in smgr.iter_smart_tags():
            tmpTrainData[j][k] = i_smart_tag.get_samples()
            raw[j][k] = i_smart_tag.get_samples()
            for i in range(int((tmpTrainData[j][k].shape[0] - 1) / 2)):
                # removing unused last channel and bipolar montage
                trainData[j][k][i] = (
                    tmpTrainData[j][k][2 * i] - tmpTrainData[j][k][2 * i + 1]
                )
            trainData[j][k] = filtfilt(b, a, trainData[j][k])
            k += 1
    train_data_players.append(trainData)


# Creation of MDM base
player1_base = Base(train_data_players[0])
player1_BASE = player1_base.Make_SPDBase()
player2_base = Base(train_data_players[1])
player2_BASE = player1_base.Make_SPDBase()
amps = TmsiCppAmplifier.get_available_amplifiers("usb")
amp = TmsiCppAmplifier(amps[0])

# Dummy amplifier for debugging
# amps = DummyCppAmplifier.get_available_amplifiers()
# amp = DummyCppAmplifier(amps[0])

Fs = 256
amp.sampling_rate = Fs

amp.start_sampling()
gains = np.array(amp.current_description.channel_gains)
offsets = np.array(amp.current_description.channel_offsets)


def samples_to_microvolts(samples):
    return samples * gains + offsets


Fs = int(Fs)

table = np.zeros((Fs * 2, channels * number_of_players))
buffer = int(Fs / 8)
buffer_counter = Fs * 2
gesture_length = Fs * 1
refraction = 0
while True:
    packet = amp.get_samples(buffer)
    tab = samples_to_microvolts(packet.samples)
    syg = tab[:, : 2 * channels * number_of_players]
    signals_montaged = np.zeros((buffer, channels * number_of_players))
    for i in range(channels * number_of_players):
        signals_montaged[:, i] = syg[:, 2 * i] - syg[:, 2 * i + 1]
    table[0:-buffer, :] = table[buffer:, :]
    table[-buffer:, :] = signals_montaged
    filtered_table = filtfilt(b, a, table, axis=0)
    player1_signal = filtered_table[-Fs:, int(player1_start / 2): int(player1_stop / 2)]
    if number_of_players == 2:
        player2_signal = filtered_table[-Fs:, player2_start // 2: player2_stop // 2]
    if buffer_counter <= 0:
        if refraction == 0:
            player1 = MDM(player1_BASE, player1_signal.T)
            player1.classify()
            player1_gesture = player1.getmin()
            if player1_gesture == 0:
                button_up()
                refraction = 0
            if player1_gesture == 1:
                button_down()
                refraction = 0
            if player1_gesture == 2:
                pass
            if number_of_players == 2:
                player2 = MDM(player2_BASE, player2_signal.T)
                player2.classify()
                player2_gesture = player2.getmin()
                if player2_gesture == 0:
                    button_w()
                if player2_gesture == 1:
                    przycisks()
                if player2_gesture == 2:
                    pass

        if refraction != 0:
            refraction -= 1
    if buffer_counter > 0:
        buffer_counter -= buffer

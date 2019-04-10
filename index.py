import numpy as np
import configparser as cp
from src import app
from obci_cpp_amplifiers.amplifiers import TmsiCppAmplifier
from obci_cpp_amplifiers.amplifiers import DummyCppAmplifier

config = cp.ConfigParser()
config.read('config.ini')
# amps = TmsiCppAmplifier.get_available_amplifiers()
# amp = TmsiCppAmplifier(amps[0])
amps = DummyCppAmplifier.get_available_amplifiers()
amp = DummyCppAmplifier(amps[0])
amp.sampling_rate = int(config['DEFAULT']['sampling_rate'])
amp.start_sampling()
gains = np.array(amp.current_description.channel_gains)
offsets = np.array(amp.current_description.channel_offsets)
prev_data = 0

def samples_to_microvolts(samples):
    return samples * gains + offsets
    
while True:
    packet = amp.get_samples(int(config['DEFAULT']['buffer_length']))
    samples = samples_to_microvolts(packet.samples)
    prev_data = app.app(samples, prev_data)


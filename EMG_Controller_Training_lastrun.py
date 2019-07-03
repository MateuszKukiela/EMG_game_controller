#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.0+brain1),
    on Fri 10 May 2019 03:56:03 PM CEST
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (
    NOT_STARTED,
    STARTED,
    PLAYING,
    PAUSED,
    STOPPED,
    FINISHED,
    PRESSED,
    RELEASED,
    FOREVER,
)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (
    sin,
    cos,
    tan,
    log,
    log10,
    pi,
    average,
    sqrt,
    std,
    deg2rad,
    rad2deg,
    linspace,
    asarray,
)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = "3.0.0+brain1"
expName = (
    "EMG_Controller_Training"
)  # from the Builder filename that created this script
expInfo = {"participant": "", "session": "001"}
import re

_force_show_dlg = False
for k, v in expInfo.items():
    m = re.match("\$(\d+):(.*)", v)
    if m:
        pos, v = m.groups()
        pos = int(pos)
        if len(sys.argv) > pos:
            v = sys.argv[pos]
        elif (not v) and (not True):
            _force_show_dlg = True
        expInfo[k] = v
if len(sys.argv) == 2:
    expInfo["participant"] = sys.argv[1]
if _force_show_dlg:
    dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo["date"] = data.getDateStr()  # add a simple timestamp
expInfo["expName"] = expName
expInfo["psychopyVersion"] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = os.path.abspath(
    os.path.expanduser(
        u"data/%s_%s_%s" % (expInfo["participant"], expName, expInfo["date"])
    )
)

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(
    name=expName,
    version="",
    extraInfo=expInfo,
    runtimeInfo=None,
    originPath="/home/fuw/MegaProjekt/EMG_Controller_Training_lastrun.py",
    savePickle=True,
    saveWideText=True,
    saveTags=True,
    dataFileName=filename,
)
# save a log file for detail verbose info
logFile = logging.LogFile(filename + ".log", level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768),
    fullscr=True,
    screen=0,
    allowGUI=False,
    allowStencil=False,
    monitor="testMonitor",
    color=[0, 0, 0],
    colorSpace="rgb",
    blendMode="avg",
    useFBO=True,
)
# store frame rate of monitor if we can measure it
expInfo["frameRate"] = win.getActualFrameRate()
if expInfo["frameRate"] != None:
    frameDur = 1.0 / round(expInfo["frameRate"])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "Instrukcja"
InstrukcjaClock = core.Clock()
text = visual.TextStim(
    win=win,
    name="text",
    text="Instrucja do eksperymentu.\nWykonuj dłonią gesty których opis pojawi się na ekranie. Każdy gest wykonaj raz po zobaczeniu tekstu. Najpierw będzie seria próbna, potem właściwa. By zacząć naciśnij spację.",
    font="Arial",
    pos=(0, 0),
    height=0.1,
    wrapWidth=None,
    ori=0,
    color="white",
    colorSpace="rgb",
    opacity=1,
    languageStyle="LTR",
    depth=0.0,
)

# Initialize components for Routine "Test"
TestClock = core.Clock()
text_2 = visual.TextStim(
    win=win,
    name="text_2",
    text="Dłoń w górę",
    font="Arial",
    pos=(0, 0),
    height=0.1,
    wrapWidth=None,
    ori=0,
    color="white",
    colorSpace="rgb",
    opacity=1,
    languageStyle="LTR",
    depth=0.0,
)
text_3 = visual.TextStim(
    win=win,
    name="text_3",
    text="Dłoń w dół",
    font="Arial",
    pos=(0, 0),
    height=0.1,
    wrapWidth=None,
    ori=0,
    color="white",
    colorSpace="rgb",
    opacity=1,
    languageStyle="LTR",
    depth=-1.0,
)
text_4 = visual.TextStim(
    win=win,
    name="text_4",
    text="Nie rób nic",
    font="Arial",
    pos=(0, 0),
    height=0.1,
    wrapWidth=None,
    ori=0,
    color="white",
    colorSpace="rgb",
    opacity=1,
    languageStyle="LTR",
    depth=-2.0,
)
text_13 = visual.TextStim(
    win=win,
    name="text_13",
    text="Wróć do pozycji wyjściowej",
    font="Arial",
    pos=(0, 0),
    height=0.1,
    wrapWidth=None,
    ori=0,
    color="white",
    colorSpace="rgb",
    opacity=1,
    languageStyle="LTR",
    depth=-3.0,
)
text_14 = visual.TextStim(
    win=win,
    name="text_14",
    text="Wróć do pozycji wyjściowej\n",
    font="Arial",
    pos=(0, 0),
    height=0.1,
    wrapWidth=None,
    ori=0,
    color="white",
    colorSpace="rgb",
    opacity=1,
    languageStyle="LTR",
    depth=-4.0,
)
text_15 = visual.TextStim(
    win=win,
    name="text_15",
    text="Wróć do pozycji wyjściowej",
    font="Arial",
    pos=(0, 0),
    height=0.1,
    wrapWidth=None,
    ori=0,
    color="white",
    colorSpace="rgb",
    opacity=1,
    languageStyle="LTR",
    depth=-5.0,
)

# Initialize components for Routine "GOGOGO"
GOGOGOClock = core.Clock()
text_5 = visual.TextStim(
    win=win,
    name="text_5",
    text="Nacisnij spację by zacząć serię właściwą.",
    font="Arial",
    pos=(0, 0),
    height=0.1,
    wrapWidth=None,
    ori=0,
    color="white",
    colorSpace="rgb",
    opacity=1,
    languageStyle="LTR",
    depth=0.0,
)

# Initialize components for Routine "Zbieranie_Danych"
Zbieranie_DanychClock = core.Clock()
text_6 = visual.TextStim(
    win=win,
    name="text_6",
    text="Dłoń w górę.",
    font="Arial",
    pos=(0, 0),
    height=0.1,
    wrapWidth=None,
    ori=0,
    color="white",
    colorSpace="rgb",
    opacity=1,
    languageStyle="LTR",
    depth=0.0,
)
text_7 = visual.TextStim(
    win=win,
    name="text_7",
    text="Dłoń w dół",
    font="Arial",
    pos=(0, 0),
    height=0.1,
    wrapWidth=None,
    ori=0,
    color="white",
    colorSpace="rgb",
    opacity=1,
    languageStyle="LTR",
    depth=-1.0,
)
text_8 = visual.TextStim(
    win=win,
    name="text_8",
    text="Nie rób nic",
    font="Arial",
    pos=(0, 0),
    height=0.1,
    wrapWidth=None,
    ori=0,
    color="white",
    colorSpace="rgb",
    opacity=1,
    languageStyle="LTR",
    depth=-2.0,
)
text_10 = visual.TextStim(
    win=win,
    name="text_10",
    text="Wróć do pozycji wyjściowej",
    font="Arial",
    pos=(0, 0),
    height=0.1,
    wrapWidth=None,
    ori=0,
    color="white",
    colorSpace="rgb",
    opacity=1,
    languageStyle="LTR",
    depth=-3.0,
)
text_11 = visual.TextStim(
    win=win,
    name="text_11",
    text="Wróć do pozycji wyjściowej\n",
    font="Arial",
    pos=(0, 0),
    height=0.1,
    wrapWidth=None,
    ori=0,
    color="white",
    colorSpace="rgb",
    opacity=1,
    languageStyle="LTR",
    depth=-4.0,
)
text_12 = visual.TextStim(
    win=win,
    name="text_12",
    text="Wróć do pozycji wyjściowej",
    font="Arial",
    pos=(0, 0),
    height=0.1,
    wrapWidth=None,
    ori=0,
    color="white",
    colorSpace="rgb",
    opacity=1,
    languageStyle="LTR",
    depth=-5.0,
)

# Initialize components for Routine "Thx"
ThxClock = core.Clock()
text_9 = visual.TextStim(
    win=win,
    name="text_9",
    text="Dziękujemy za współpracę :)",
    font="Arial",
    pos=(0, 0),
    height=0.1,
    wrapWidth=None,
    ori=0,
    color="white",
    colorSpace="rgb",
    opacity=1,
    languageStyle="LTR",
    depth=0.0,
)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = (
    core.CountdownTimer()
)  # to track time remaining of each (non-slip) routine

# ------Prepare to start Routine "Instrukcja"-------
t = 0
InstrukcjaClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
text.setTagName("")
text.setTagParams({})
key_resp_2 = event.BuilderKeyResponse()
# keep track of which components have finished
InstrukcjaComponents = [text, key_resp_2]
for thisComponent in InstrukcjaComponents:
    if hasattr(thisComponent, "status"):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instrukcja"-------
while continueRoutine:
    # get current time
    t = InstrukcjaClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)

    # *key_resp_2* updates
    if t >= 2 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType="keyboard")
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=["space"])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = (
        False
    )  # will revert to True if at least one component still running
    for thisComponent in InstrukcjaComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if (
        continueRoutine
    ):  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instrukcja"-------
for thisComponent in InstrukcjaComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
    if hasattr(thisComponent, "tagID"):
        thisExp.setEndTimeInTag(thisComponent.tagID)
# check responses
if key_resp_2.keys in ["", [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData("key_resp_2.keys", key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData("key_resp_2.rt", key_resp_2.rt)
thisExp.nextEntry()
# the Routine "Instrukcja" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(
    nReps=2,
    method="random",
    extraInfo=expInfo,
    originPath=-1,
    trialList=[None],
    seed=None,
    name="trials",
)
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec("{} = thisTrial[paramName]".format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec("{} = thisTrial[paramName]".format(paramName))

    # ------Prepare to start Routine "Test"-------
    t = 0
    TestClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(9.000000)
    # update component parameters for each repeat
    text_2.setTagName("")
    text_2.setTagParams({})
    text_3.setTagName("")
    text_3.setTagParams({})
    text_4.setTagName("")
    text_4.setTagParams({})
    text_13.setTagName("")
    text_13.setTagParams({})
    text_14.setTagName("")
    text_14.setTagParams({})
    text_15.setTagName("")
    text_15.setTagParams({})
    # keep track of which components have finished
    TestComponents = [text_2, text_3, text_4, text_13, text_14, text_15]
    for thisComponent in TestComponents:
        if hasattr(thisComponent, "status"):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "Test"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = TestClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *text_2* updates
        if t >= 0.0 and text_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_2.tStart = t
            text_2.frameNStart = frameN  # exact frame index
            text_2.setAutoDraw(True)
        frameRemains = (
            0.0 + 2 - win.monitorFramePeriod * 0.75
        )  # most of one frame period left
        if text_2.status == STARTED and t >= frameRemains:
            text_2.setAutoDraw(False)

        # *text_3* updates
        if t >= 3 and text_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_3.tStart = t
            text_3.frameNStart = frameN  # exact frame index
            text_3.setAutoDraw(True)
        frameRemains = (
            3 + 2 - win.monitorFramePeriod * 0.75
        )  # most of one frame period left
        if text_3.status == STARTED and t >= frameRemains:
            text_3.setAutoDraw(False)

        # *text_4* updates
        if t >= 6 and text_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_4.tStart = t
            text_4.frameNStart = frameN  # exact frame index
            text_4.setAutoDraw(True)
        frameRemains = (
            6 + 2 - win.monitorFramePeriod * 0.75
        )  # most of one frame period left
        if text_4.status == STARTED and t >= frameRemains:
            text_4.setAutoDraw(False)

        # *text_13* updates
        if t >= 2 and text_13.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_13.tStart = t
            text_13.frameNStart = frameN  # exact frame index
            text_13.setAutoDraw(True)
        frameRemains = (
            2 + 1.0 - win.monitorFramePeriod * 0.75
        )  # most of one frame period left
        if text_13.status == STARTED and t >= frameRemains:
            text_13.setAutoDraw(False)

        # *text_14* updates
        if t >= 5 and text_14.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_14.tStart = t
            text_14.frameNStart = frameN  # exact frame index
            text_14.setAutoDraw(True)
        frameRemains = (
            5 + 1.0 - win.monitorFramePeriod * 0.75
        )  # most of one frame period left
        if text_14.status == STARTED and t >= frameRemains:
            text_14.setAutoDraw(False)

        # *text_15* updates
        if t >= 8 and text_15.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_15.tStart = t
            text_15.frameNStart = frameN  # exact frame index
            text_15.setAutoDraw(True)
        frameRemains = (
            8 + 1.0 - win.monitorFramePeriod * 0.75
        )  # most of one frame period left
        if text_15.status == STARTED and t >= frameRemains:
            text_15.setAutoDraw(False)

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = (
            False
        )  # will revert to True if at least one component still running
        for thisComponent in TestComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if (
            continueRoutine
        ):  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "Test"-------
    for thisComponent in TestComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
        if hasattr(thisComponent, "tagID"):
            thisExp.setEndTimeInTag(thisComponent.tagID)
    thisExp.nextEntry()

# completed 2 repeats of 'trials'


# ------Prepare to start Routine "GOGOGO"-------
t = 0
GOGOGOClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
text_5.setTagName("")
text_5.setTagParams({})
key_resp_3 = event.BuilderKeyResponse()
# keep track of which components have finished
GOGOGOComponents = [text_5, key_resp_3]
for thisComponent in GOGOGOComponents:
    if hasattr(thisComponent, "status"):
        thisComponent.status = NOT_STARTED

# -------Start Routine "GOGOGO"-------
while continueRoutine:
    # get current time
    t = GOGOGOClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *text_5* updates
    if t >= 0.0 and text_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_5.tStart = t
        text_5.frameNStart = frameN  # exact frame index
        text_5.setAutoDraw(True)

    # *key_resp_3* updates
    if t >= 0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType="keyboard")
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys(keyList=["space"])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_3.keys = theseKeys[-1]  # just the last key pressed
            key_resp_3.rt = key_resp_3.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = (
        False
    )  # will revert to True if at least one component still running
    for thisComponent in GOGOGOComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if (
        continueRoutine
    ):  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "GOGOGO"-------
for thisComponent in GOGOGOComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
    if hasattr(thisComponent, "tagID"):
        thisExp.setEndTimeInTag(thisComponent.tagID)
# check responses
if key_resp_3.keys in ["", [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData("key_resp_3.keys", key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData("key_resp_3.rt", key_resp_3.rt)
thisExp.nextEntry()
# the Routine "GOGOGO" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(
    nReps=10,
    method="random",
    extraInfo=expInfo,
    originPath=-1,
    trialList=[None],
    seed=None,
    name="trials_2",
)
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec("{} = thisTrial_2[paramName]".format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec("{} = thisTrial_2[paramName]".format(paramName))

    # ------Prepare to start Routine "Zbieranie_Danych"-------
    t = 0
    Zbieranie_DanychClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(10.500000)
    # update component parameters for each repeat
    text_6.setTagName("gora")
    text_6.setTagParams({})
    text_7.setTagName("dol")
    text_7.setTagParams({})
    text_8.setTagName("piesc")
    text_8.setTagParams({})
    text_10.setTagName("")
    text_10.setTagParams({})
    text_11.setTagName("")
    text_11.setTagParams({})
    text_12.setTagName("")
    text_12.setTagParams({})
    # keep track of which components have finished
    Zbieranie_DanychComponents = [text_6, text_7, text_8, text_10, text_11, text_12]
    for thisComponent in Zbieranie_DanychComponents:
        if hasattr(thisComponent, "status"):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "Zbieranie_Danych"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Zbieranie_DanychClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *text_6* updates
        if t >= 0.0 and text_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_6.tStart = t
            text_6.frameNStart = frameN  # exact frame index
            text_6.tagID = thisExp.setStartTimeInTag("gora", {})
            text_6.setAutoDraw(True)
        frameRemains = (
            0.0 + 1.5 - win.monitorFramePeriod * 0.75
        )  # most of one frame period left
        if text_6.status == STARTED and t >= frameRemains:
            thisExp.setEndTimeInTag(text_6.tagID)
            text_6.setAutoDraw(False)

        # *text_7* updates
        if t >= 3.5 and text_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_7.tStart = t
            text_7.frameNStart = frameN  # exact frame index
            text_7.tagID = thisExp.setStartTimeInTag("dol", {})
            text_7.setAutoDraw(True)
        frameRemains = (
            3.5 + 1.5 - win.monitorFramePeriod * 0.75
        )  # most of one frame period left
        if text_7.status == STARTED and t >= frameRemains:
            thisExp.setEndTimeInTag(text_7.tagID)
            text_7.setAutoDraw(False)

        # *text_8* updates
        if t >= 7 and text_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_8.tStart = t
            text_8.frameNStart = frameN  # exact frame index
            text_8.tagID = thisExp.setStartTimeInTag("piesc", {})
            text_8.setAutoDraw(True)
        frameRemains = (
            7 + 1.5 - win.monitorFramePeriod * 0.75
        )  # most of one frame period left
        if text_8.status == STARTED and t >= frameRemains:
            thisExp.setEndTimeInTag(text_8.tagID)
            text_8.setAutoDraw(False)

        # *text_10* updates
        if t >= 1.5 and text_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_10.tStart = t
            text_10.frameNStart = frameN  # exact frame index
            text_10.setAutoDraw(True)
        frameRemains = (
            1.5 + 2 - win.monitorFramePeriod * 0.75
        )  # most of one frame period left
        if text_10.status == STARTED and t >= frameRemains:
            text_10.setAutoDraw(False)

        # *text_11* updates
        if t >= 5 and text_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_11.tStart = t
            text_11.frameNStart = frameN  # exact frame index
            text_11.setAutoDraw(True)
        frameRemains = (
            5 + 2 - win.monitorFramePeriod * 0.75
        )  # most of one frame period left
        if text_11.status == STARTED and t >= frameRemains:
            text_11.setAutoDraw(False)

        # *text_12* updates
        if t >= 8.5 and text_12.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_12.tStart = t
            text_12.frameNStart = frameN  # exact frame index
            text_12.setAutoDraw(True)
        frameRemains = (
            8.5 + 2 - win.monitorFramePeriod * 0.75
        )  # most of one frame period left
        if text_12.status == STARTED and t >= frameRemains:
            text_12.setAutoDraw(False)

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = (
            False
        )  # will revert to True if at least one component still running
        for thisComponent in Zbieranie_DanychComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if (
            continueRoutine
        ):  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "Zbieranie_Danych"-------
    for thisComponent in Zbieranie_DanychComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
        if hasattr(thisComponent, "tagID"):
            thisExp.setEndTimeInTag(thisComponent.tagID)
    thisExp.nextEntry()

# completed 10 repeats of 'trials_2'


# ------Prepare to start Routine "Thx"-------
t = 0
ThxClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
text_9.setTagName("")
text_9.setTagParams({})
# keep track of which components have finished
ThxComponents = [text_9]
for thisComponent in ThxComponents:
    if hasattr(thisComponent, "status"):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Thx"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ThxClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *text_9* updates
    if t >= 0.0 and text_9.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_9.tStart = t
        text_9.frameNStart = frameN  # exact frame index
        text_9.setAutoDraw(True)
    frameRemains = (
        0.0 + 3 - win.monitorFramePeriod * 0.75
    )  # most of one frame period left
    if text_9.status == STARTED and t >= frameRemains:
        text_9.setAutoDraw(False)

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = (
        False
    )  # will revert to True if at least one component still running
    for thisComponent in ThxComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if (
        continueRoutine
    ):  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Thx"-------
for thisComponent in ThxComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
    if hasattr(thisComponent, "tagID"):
        thisExp.setEndTimeInTag(thisComponent.tagID)
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename + ".csv")
thisExp.saveAsPickle(filename)
thisExp.saveAsTags(filename + ".tag")
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

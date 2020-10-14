#script for a pilot experiment on perception of morphed sounds (human voices, instruments) with 4 different experimental blocks

#-------------------------------------------------------------------------------------
#details
#
#
#
#
#CAVE: exportet data file gives ##### fileds or incorrect high numbners for some ISI and reaction time values. This is due to an encoding/decoding problem with excel. It works fine by importing the .csv into R!
#-------------------------------------------------------------------------------------

#libraries
from __future__ import absolute_import, division
from psychopy.sound import Sound
from psychopy import core, visual, gui, data, event, sound, prefs, locale_setup, logging 
from psychopy.tools.filetools import fromFile, toFile
from psychopy.constants import (NOT_STARTED, STARTED, FINISHED)
import numpy, random, csv, time, sys, os
import pandas as pd
import psychtoolbox as ptb
import psychopy.visual
from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
#_thisDir = os.path.dirname(os.path.abspath(__file__))
#os.chdir(_thisDir)



#Store info about the experiment session
# --------------------------------------------
expName 			= u'Pilot_experiment'  # from the Builder filename that created this script
expInfo 			= {'participant':'', 'condition':'','use trigger':False}
dlg 				= gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK 			== False: core.quit()  # user pressed cancel
expInfo['date'] 	= data.getDateStr()  # add a simple timestamp
expInfo['expName'] 	= expName


#Trigger
#---------------------------------------------
global useTrigger
useTrigger = False

if expInfo['use trigger']:
    useTrigger = True
    

    
#make a text file to save data
# --------------------------------------------
fileName = u"data/" + expInfo['condition']+'_' + expInfo[u'participant'] +'_'+expInfo['date'] + "/" +  expInfo['expName']+ "_"+expInfo[u'participant']
os.makedirs("data/" + expInfo['condition']+'_' + expInfo[u'participant'] +'_'+ expInfo['date'] + "/")

# save a log file for detail verbose info
logFile = logging.LogFile(fileName+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file


#create a window
#---------------------------------------------
global mywin
mywin = visual.Window(size=(1280, 1024), fullscr=True, screen=0,monitor='testMonitor', winType='pyglet', color='black', colorSpace='rgb', blendMode='avg',useFBO=True, waitBlanking=True)
expInfo['frameRate']=mywin.getActualFrameRate() #frame rate


endExpNow = False  # flag for 'escape' or other condition => quit the exp

    
# psychopy experiment handler
thisExp = data.ExperimentHandler(name=expName, version='',
    					extraInfo=expInfo, runtimeInfo=None,
    					originPath=None,
    					savePickle=True, saveWideText=True,
    					dataFileName=fileName)
    
#add a clock to keep track of time
#---------------------------------------------
trialClock 			= core.Clock() # initialise: trial clock measures reaction times relative to sound onset
scannerClock        =core.Clock() #initialise clock to measure time relative to scanner start (trigger "T")




###############################################################################
#create/load stimuli
###############################################################################

#Blocks
#---------------------------------------------
#randomisation of trials per experimental block are created outside this script beforehand to save time

blocks 				= ['Gen', 'Ins', 'Tim', 'Voc']
Ntrials             = [4*24,4*48, 4*72, 4*48] #four repetitions per item
Ntotal              = 4*24 +4*48 + 4*48 + 4*72
order 				= [0,1,2,3]
numpy.random.shuffle(order)

#ISI should be jitterted between 3 and 5 seconds in steps of 200ms
ISI_range 			= numpy.arange(3, 5.2, 0.2)


#instructions
#---------------------------------------------
instr_gen = visual.TextStim(win=mywin, ori=0, name='instr_gen',
    					text="Welcome!\n\nYou are going to hear sounds, that either are  human voices, musical instruments or a mixture of both. You will have different tasks to solve in each block of the experiment and you always have to chose an answer of two options for each sound.\nFor example, you have to decide, whether a sound is a human voice or not a human voice.\n\nPlease respond in any case, even if you are not totally sure about the answer. There is no correct answer. Please give the answer that fits best to your perception of the sound!\n\nPress 'space' to continue.\n",    font='Arial',
    					pos=[0, 0], height=0.06, wrapWidth=None,
    					color='white', colorSpace='rgb', opacity=1,
    					depth=0.0)


#specific information on task of respective block
#specific information on task of respective block
instr_genderA = "Gender-Task\n\nIn the following block of the experiment please decide for each sound, whether you think it is a female or a male voice.\n\n\n\n\n\n\n\n\n\n\n\n\nPlease press 'green' for 'female' and 'red' for 'male'. Please use the index finger and the middle finger of your right hand. Duration: ca. 6,5 min.\n\nTo start with the task, press 'space'"

instr_timbreA = "Timbre-Task\n\nIn the following block of the experiment please decide for each sound, whether you think it is a string instrument or a woodwind instrument.\n\n\n\n\n\n\n\n\n\n\n\n\n\nPlease press 'green' for 'string' and 'red' for 'woodwind' instrument. Please use the index finger and the middle finger of your right hand. Duration: ca. 20 min.\n\nTo start with the task, press 'space'"

instr_instrumentA = "Instrument-Task\n\nIn the following block of the experiment please decide for each sound, whether you think it is a musical instrument or not a musical instrument.\n\n\n\n\n\n\n\n\n\n\n\n\n\nPlease press 'green' for 'musical instrument' and 'red' for 'not a musical instrument'. Please use the index finger and the middle finger of your right hand. Duration ca. 13 min.\n\nTo start with the task, press 'space'"

instr_voiceA = "Voice-Task\n\nIn the following block of the experiment please decide for each sound, whether you think it is a human voice or not a human voice\n\n\n\n\n\n\n\n\n\n\n\n\n\nPlease press 'green' for 'human voice' and 'red' for 'not a human voice'. Please use the index finger and the middle finger of your right hand. Duration: ca. 13 min.\n\nTo start with the task, press 'space'"

instr_genderB = "Gender-Task\n\nIn the following block of the experiment please decide for each sound, whether you think it is a female or a male voice.\n\n\n\n\n\n\n\n\n\n\n\n\nPlease press 'green' for 'male' and 'red' for 'female'. Please use the index finger and the middle finger of your right hand. Duration: ca. 6,5 min.\n\nTo start with the task, press 'space'"

instr_timbreB = "Timbre-Task\n\nIn the following block of the experiment please decide for each sound, whether you think it is a string instrument or a woodwind instrument.\n\n\n\n\n\n\n\n\n\n\n\n\n\nPlease press 'green' for 'woodwind' and 'red' for 'string' instrument. Please use the index finger and the middle finger of your right hand. Duration: ca. 20 min.\n\nTo start with the task, press 'space'"

instr_instrumentB = "Instrument-Task\n\nIn the following block of the experiment please decide for each sound, whether you think it is a musical instrument or not a musical instrument.\n\n\n\n\n\n\n\n\n\n\n\n\n\nPlease press 'green' for 'not a musical instrument' and 'red' for 'musical instrument'. Please use the index finger and the middle finger of your right hand. Duration ca. 13 min.\n\nTo start with the task, press 'space'"

instr_voiceB = "Voice-Task\n\nIn the following block of the experiment please decide for each sound, whether you think it is a human voice or not a human voice\n\n\n\n\n\n\n\n\n\n\n\n\n\nPlease press 'green' for 'not a human voice' and 'red' for 'human voice'. Please use the index finger and the middle finger of your right hand. Duration: ca. 13 min.\n\nTo start with the task, press 'space'"


#images for instruction (two versions of button responses A and B)

img_genderA = psychopy.visual.ImageStim(win=mywin,image="gender.png", units="pix")
img_timbreA = psychopy.visual.ImageStim(win=mywin,image="timbre.png", units="pix")
img_instrumentA = psychopy.visual.ImageStim(win=mywin,image="instrument.png", units="pix")
img_voiceA = psychopy.visual.ImageStim(win=mywin,image="voice.png", units="pix")

img_genderB = psychopy.visual.ImageStim(win=mywin,image="gender_B.png", units="pix")
img_timbreB = psychopy.visual.ImageStim(win=mywin,image="timbre_B.png", units="pix")
img_instrumentB = psychopy.visual.ImageStim(win=mywin,image="instrument_B.png", units="pix")
img_voiceB = psychopy.visual.ImageStim(win=mywin,image="voice_B.png", units="pix")

#select instructions for button presses depending on version
if expInfo['condition']=='A':
    images              = [img_genderA, img_instrumentA, img_timbreA, img_voiceA]
    instructions        = [instr_genderA, instr_instrumentA, instr_timbreA, instr_voiceA]
if expInfo['condition']=='B':
    images              = [img_genderB, img_instrumentB, img_timbreB, img_voiceB]
    instructions        = [instr_genderB, instr_instrumentB, instr_timbreB, instr_voiceB]



#######################################################################
#Experiment
#######################################################################


#general instruction page
#---------------------------------------------


instr_gen.setAutoDraw(True)

mywin.flip()

#continue to next page with 'space'
end = True
while end:
    for key in event.getKeys():
        if key in ['escape']: 
            mywin.close()
            core.quit()
        if key in ['space']:
            end = False
        
        

instr_gen.setAutoDraw(False)


mywin.flip()





# conditions file and variables
#---------------------------------------------      

#arrays for variables of conditions file, read into data frame

ExpConditions = pd.read_csv("..\\Experiment_trials\\all_conditions_rand.csv") 
ExpConditions.head()

#select columns via: ExpConditions.'columnname'

#-----------------------------------
####################################
#first experimental task 
####################################
#-----------------------------------

#prepare to start trials

thistask 			= blocks[order[0]] # current block
thistrials 			= ExpConditions[ExpConditions["Block"] == thistask] #trials for this block
thisinstruction 	= instructions[order[0]]# instruction for this block
thisimage           = images[order[0]]#set instruction image for block
thisN 				= Ntrials[order[0]] #number of trials for this block
thisISI_jitter 		= numpy.random.choice(ISI_range, thisN, replace=True) #creates jitter by randomly choosing from the ISI_range with replacement. (ISI might not be fully equally distributed)
thisSound 			= sound.Sound('A', secs=10) #initialise sound
kb 					= keyboard.Keyboard() #initialise keyboard 
kb.keys 			= []
kb.rt 				= []



#block instruction
#------------------------------------------------

instr_thisblock = visual.TextStim(win=mywin, ori=0, name='instr_voice',
    					text=thisinstruction,    font='Arial',
   						pos=[0, 0], height=0.06, wrapWidth=None,
    					color='white', colorSpace='rgb', opacity=1,
    					depth=0.0)

instr_thistask = visual.TextStim(win=mywin, ori=0, name='instr_voice',
    					text=thistask,    font='Arial',
    					pos=[0, 0], height=0.1, wrapWidth=None,
    					color='white', colorSpace='rgb', opacity=1,
    					depth=0.0)

instr_thisblock.setAutoDraw(True)
thisimage.setAutoDraw(True)
mywin.flip()

end = True
while end:
    for key in event.getKeys():
        if key in ['escape']: 
            mywin.close()
            core.quit()
        if key in ['space']: #trigger from Scanner to start experiment
            scannerClock.reset() #reset and start time measurement of scanner
            end = False
        
        

instr_thisblock.setAutoDraw(False)

mywin.flip()
core.wait(10)


#start of trials

trial_num = 0
end = True
#key2 = event.BuilderKeyResponse() 
#instruction of block


#blank period between  isntruction and trials

mywin.flip()
while end:
    # exit if trial limit reached
    if trial_num >= (thisN-1):
        thisSound.stop()
        end = False
    if trial_num >= 0:
        # start time measurement
        trialClock.reset()
        kb.clock.reset()
        kb.clearEvents(eventType='keyboard')
        #draw button press instruction to screen
        
        
        
        #select and start sound
        thisSound.setSound(thistrials.iloc[trial_num, 9])
        thisSound.play()
        thistrial_time = scannerClock.getTime()
        mywin.flip()
        mywin.flip()
        # send trigger by sound
        if useTrigger:
            Trigger().send('sound')
        
        # set conditions
        
        trial_finished = 0
        while trial_finished == 0:
            t = trialClock.getTime()
            keys = kb.getKeys(['right','left','escape'])
            
            # end trial if duration > 6s + thisISI_jitter
            if t >= (0.6+thisISI_jitter[trial_num]):
                thisSound.stop()
                trial_finished = 1
                #mywin.flip()
                
            # trigger events for escape key
            for key in keys:
                if key in ['escape']: 
                    thisSound.stop()
                    mywin.close()
                    core.quit() 
            if len(keys):
                #if useTrigger:
                #    Trigger().send('key')
                key2= keys[0]  # at least one key was pressed 
                kb.keys = key2.name  # just the last key pressed
                kb.rt = round(key2.rt,5)        
        
        # write trial data to csv
        thisExp.addData('trialnr', thistrials.iloc[trial_num, 0])
        thisExp.addData('trial', thistrials.iloc[trial_num, 1])
        thisExp.addData('Block', thistrials.iloc[trial_num, 2])
        thisExp.addData('Category1', thistrials.iloc[trial_num, 3])
        thisExp.addData('Prototype1', thistrials.iloc[trial_num, 4])
        thisExp.addData('Category2', thistrials.iloc[trial_num, 5])
        thisExp.addData('Prototype2', thistrials.iloc[trial_num, 6])
        thisExp.addData('morphrate1', thistrials.iloc[trial_num, 7])
        thisExp.addData('morphrate2', thistrials.iloc[trial_num, 8])
        thisExp.addData('names', thistrials.iloc[trial_num, 9])
        thisExp.addData('ISI_jitter', str(thisISI_jitter[trial_num]))
        if kb.keys in ['', [], None]:  # No response was made
            kb.keys = None
        thisExp.addData('key',kb.keys)
        
        thisExp.addData('rt', kb.rt)
        
        #save information if sound was sucessfully played in data file
        if thisSound.status == NOT_STARTED:
            play=0
        elif thisSound.status == STARTED:
            play = 1
        elif thisSound.status == FINISHED:
            play = 2
            
        thisExp.addData('play', play)
        thisExp.addData('onset', thistrial_time)
        thisExp.nextEntry()
        trial_num += 1
#---------------------------------------------

#cleanup
thisimage.setAutoDraw(False)




#-----------------------------------
####################################
#Block 2
####################################
#-----------------------------------

#prepare to start trials

thistask 			= blocks[order[1]] # current block
thistrials 			= ExpConditions[ExpConditions["Block"] == thistask] #trials for this block
thisinstruction 	= instructions[order[1]]# instruction for this block
thisimage           = images[order[1]]#set instruction image for block#button press instruction during trials for this block
thisN 				= Ntrials[order[1]] #number of trials for this block
thisISI_jitter 		= numpy.random.choice(ISI_range, thisN, replace=True) #creates jitter by randomly choosing from the ISI_range with replacement. (ISI might not be fully equally distributed)
thisSound 			= sound.Sound('A', secs=10) #initialise sound
kb 					= keyboard.Keyboard() #initialise keyboard 
kb.keys 			= []
kb.rt 				= []



#block instruction
#------------------------------------------------

instr_thisblock = visual.TextStim(win=mywin, ori=0, name='instr_voice',
    					text=thisinstruction,    font='Arial',
   						pos=[0, 0], height=0.06, wrapWidth=None,
    					color='white', colorSpace='rgb', opacity=1,
    					depth=0.0)

instr_thistask = visual.TextStim(win=mywin, ori=0, name='instr_voice',
    					text=thistask,    font='Arial',
    					pos=[0, 0], height=0.1, wrapWidth=None,
    					color='white', colorSpace='rgb', opacity=1,
    					depth=0.0)

instr_thisblock.setAutoDraw(True)
thisimage.setAutoDraw(True)

mywin.flip()

end = True
while end:
    for key in event.getKeys():
        if key in ['escape']: 
            mywin.close()
            core.quit()
        if key in ['space']:
            end = False
        
        

instr_thisblock.setAutoDraw(False)

mywin.flip()
core.wait(10)


#start of trials

trial_num = 0
end = True
#key2 = event.BuilderKeyResponse() 
#instruction of block


#blank period between  instruction and trials

mywin.flip()
while end:
    # exit if trial limit reached
    if trial_num >= (thisN-1):
        thisSound.stop()
        end = False
    if trial_num >= 0:
        # start time measurement
        trialClock.reset()
        kb.clock.reset()
        kb.clearEvents(eventType='keyboard')
        #draw button press instruction to screen
        
        
        
        #select and start sound
        thisSound.setSound(thistrials.iloc[trial_num, 9])
        thisSound.play()
        thistrial_time = scannerClock.getTime()
        mywin.flip()
        # send trigger by sound
        if useTrigger:
            Trigger().send('sound')
        
        # set conditions
        
        trial_finished = 0
        while trial_finished == 0:
            t = trialClock.getTime()
            keys = kb.getKeys(['right','left','escape'])
            
            # end trial if duration > 6s + thisISI_jitter
            if t >= (0.6+thisISI_jitter[trial_num]):
                thisSound.stop()
                trial_finished = 1
                #mywin.flip()
                
            # trigger events for escape key
            for key in keys:
                if key in ['escape']: 
                    thisSound.stop()
                    mywin.close()
                    core.quit() 
            if len(keys):
                #if useTrigger:
                #    Trigger().send('key')
                key2= keys[0]  # at least one key was pressed 
                kb.keys = key2.name  # just the last key pressed
                kb.rt = round(key2.rt,5)        
        
        # write trial data to csv
        thisExp.addData('trialnr', thistrials.iloc[trial_num, 0])
        thisExp.addData('trial', thistrials.iloc[trial_num, 1])
        thisExp.addData('Block', thistrials.iloc[trial_num, 2])
        thisExp.addData('Category1', thistrials.iloc[trial_num, 3])
        thisExp.addData('Prototype1', thistrials.iloc[trial_num, 4])
        thisExp.addData('Category2', thistrials.iloc[trial_num, 5])
        thisExp.addData('Prototype2', thistrials.iloc[trial_num, 6])
        thisExp.addData('morphrate1', thistrials.iloc[trial_num, 7])
        thisExp.addData('morphrate2', thistrials.iloc[trial_num, 8])
        thisExp.addData('names', thistrials.iloc[trial_num, 9])
        thisExp.addData('ISI_jitter', str(thisISI_jitter[trial_num]))
        if kb.keys in ['', [], None]:  # No response was made
            kb.keys = None
        thisExp.addData('key',kb.keys)
        
        thisExp.addData('rt', kb.rt)
        
        #save information if sound was sucessfully played in data file
        if thisSound.status == NOT_STARTED:
            play=0
        elif thisSound.status == STARTED:
            play = 1
        elif thisSound.status == FINISHED:
            play = 2
            
        thisExp.addData('play', play)
        thisExp.addData('onset', thistrial_time)
        thisExp.nextEntry()
        trial_num += 1
#---------------------------------------------

#cleanup
thisimage.setAutoDraw(False)



#-----------------------------------
####################################
#Block 3
####################################
#-----------------------------------

#prepare to start trials

thistask 			= blocks[order[2]] # current block
thistrials 			= ExpConditions[ExpConditions["Block"] == thistask] #trials for this block
thisinstruction 	= instructions[order[2]]# instruction for this block
thisimage           = images[order[2]]#set instruction image for block
thisN 				= Ntrials[order[2]] #number of trials for this block
thisISI_jitter 		= numpy.random.choice(ISI_range, thisN, replace=True) #creates jitter by randomly choosing from the ISI_range with replacement. (ISI might not be fully equally distributed)
thisSound 			= sound.Sound('A', secs=10) #initialise sound
kb 					= keyboard.Keyboard() #initialise keyboard 
kb.keys 			= []
kb.rt 				= []



#block instruction
#------------------------------------------------

instr_thisblock = visual.TextStim(win=mywin, ori=0, name='instr_voice',
    					text=thisinstruction,    font='Arial',
   						pos=[0, 0], height=0.06, wrapWidth=None,
    					color='white', colorSpace='rgb', opacity=1,
    					depth=0.0)

instr_thistask = visual.TextStim(win=mywin, ori=0, name='instr_voice',
    					text=thistask,    font='Arial',
    					pos=[0, 0], height=0.1, wrapWidth=None,
    					color='white', colorSpace='rgb', opacity=1,
    					depth=0.0)

instr_thisblock.setAutoDraw(True)
thisimage.setAutoDraw(True)
mywin.flip()

end = True
while end:
    for key in event.getKeys():
        if key in ['escape']: 
            mywin.close()
            core.quit()
        if key in ['space']:
            end = False
        
        

instr_thisblock.setAutoDraw(False)

mywin.flip()
core.wait(10)


#start of trials

trial_num = 0
end = True
#key2 = event.BuilderKeyResponse() 
#instruction of block


#blank period between  isntruction and trials

mywin.flip()
while end:
    # exit if trial limit reached
    if trial_num >= (thisN-1):
        thisSound.stop()
        end = False
    if trial_num >= 0:
        # start time measurement
        trialClock.reset()
        kb.clock.reset()
        kb.clearEvents(eventType='keyboard')
        #draw button press instruction to screen
        
        
        
        #select and start sound
        thisSound.setSound(thistrials.iloc[trial_num, 9])
        thisSound.play()
        thistrial_time = scannerClock.getTime()
        mywin.flip()
        # send trigger by sound
        if useTrigger:
            Trigger().send('sound')
        
        # set conditions
        
        trial_finished = 0
        while trial_finished == 0:
            t = trialClock.getTime()
            keys = kb.getKeys(['right','left','escape'])
            
            # end trial if duration > 6s + thisISI_jitter
            if t >= (0.6+thisISI_jitter[trial_num]):
                thisSound.stop()
                trial_finished = 1
                #mywin.flip()
                
            # trigger events for escape key
            for key in keys:
                if key in ['escape']: 
                    thisSound.stop()
                    mywin.close()
                    core.quit() 
            if len(keys):
                #if useTrigger:
                #    Trigger().send('key')
                key2= keys[0]  # at least one key was pressed 
                kb.keys = key2.name  # just the last key pressed
                kb.rt = round(key2.rt,5)        
        
        # write trial data to csv
        thisExp.addData('trialnr', thistrials.iloc[trial_num, 0])
        thisExp.addData('trial', thistrials.iloc[trial_num, 1])
        thisExp.addData('Block', thistrials.iloc[trial_num, 2])
        thisExp.addData('Category1', thistrials.iloc[trial_num, 3])
        thisExp.addData('Prototype1', thistrials.iloc[trial_num, 4])
        thisExp.addData('Category2', thistrials.iloc[trial_num, 5])
        thisExp.addData('Prototype2', thistrials.iloc[trial_num, 6])
        thisExp.addData('morphrate1', thistrials.iloc[trial_num, 7])
        thisExp.addData('morphrate2', thistrials.iloc[trial_num, 8])
        thisExp.addData('names', thistrials.iloc[trial_num, 9])
        thisExp.addData('ISI_jitter', str(thisISI_jitter[trial_num]))
        if kb.keys in ['', [], None]:  # No response was made
            kb.keys = None
        thisExp.addData('key',kb.keys)
        
        thisExp.addData('rt', kb.rt)
        
        #save information if sound was sucessfully played in data file
        if thisSound.status == NOT_STARTED:
            play=0
        elif thisSound.status == STARTED:
            play = 1
        elif thisSound.status == FINISHED:
            play = 2
            
        thisExp.addData('play', play)
        thisExp.addData('onset', thistrial_time)
        thisExp.nextEntry()
        trial_num += 1
#---------------------------------------------

#cleanup
thisimage.setAutoDraw(False)


#-----------------------------------
####################################
#Block 4
####################################
#-----------------------------------

#prepare to start trials

thistask 			= blocks[order[3]] # current block
thistrials 			= ExpConditions[ExpConditions["Block"] == thistask] #trials for this block
thisinstruction 	= instructions[order[3]]# instruction for this block
thisimage           = images[order[3]]#set instruction image for block
thisN 				= Ntrials[order[3]] #number of trials for this block
thisISI_jitter 		= numpy.random.choice(ISI_range, thisN, replace=True) #creates jitter by randomly choosing from the ISI_range with replacement. (ISI might not be fully equally distributed)
thisSound 			= sound.Sound('A', secs=10) #initialise sound
kb 					= keyboard.Keyboard() #initialise keyboard 
kb.keys 			= []
kb.rt 				= []



#block instruction
#------------------------------------------------

instr_thisblock = visual.TextStim(win=mywin, ori=0, name='instr_voice',
    					text=thisinstruction,    font='Arial',
   						pos=[0, 0], height=0.06, wrapWidth=None,
    					color='white', colorSpace='rgb', opacity=1,
    					depth=0.0)

instr_thistask = visual.TextStim(win=mywin, ori=0, name='instr_voice',
    					text=thistask,    font='Arial',
    					pos=[0, 0], height=0.1, wrapWidth=None,
    					color='white', colorSpace='rgb', opacity=1,
    					depth=0.0)

instr_thisblock.setAutoDraw(True)
thisimage.setAutoDraw(True)
mywin.flip()

end = True
while end:
    for key in event.getKeys():
        if key in ['escape']: 
            mywin.close()
            core.quit()
        if key in ['space']:
            end = False
        
        

instr_thisblock.setAutoDraw(False)

mywin.flip()
core.wait(10)


#start of trials

trial_num = 0
end = True
#key2 = event.BuilderKeyResponse() 
#instruction of block


#blank period between  isntruction and trials

mywin.flip()
while end:
    # exit if trial limit reached
    if trial_num >= (thisN-1):
        thisSound.stop()
        end = False
    if trial_num >= 0:
        # start time measurement
        trialClock.reset()
        kb.clock.reset()
        kb.clearEvents(eventType='keyboard')
        #draw button press instruction to screen
        
        
        
        #select and start sound
        thisSound.setSound(thistrials.iloc[trial_num, 9])
        thisSound.play()
        thistrial_time = scannerClock.getTime()
        mywin.flip()
        # send trigger by sound
        if useTrigger:
            Trigger().send('sound')
        
        # set conditions
        
        trial_finished = 0
        while trial_finished == 0:
            t = trialClock.getTime()
            keys = kb.getKeys(['right','left','escape'])
            
            # end trial if duration > 6s + thisISI_jitter
            if t >= (0.6+thisISI_jitter[trial_num]):
                thisSound.stop()
                trial_finished = 1
                #mywin.flip()
                
            # trigger events for escape key
            for key in keys:
                if key in ['escape']: 
                    thisSound.stop()
                    mywin.close()
                    core.quit() 
            if len(keys):
                #if useTrigger:
                #    Trigger().send('key')
                key2= keys[0]  # at least one key was pressed 
                kb.keys = key2.name  # just the last key pressed
                kb.rt = round(key2.rt,5)        
        
        # write trial data to csv
        thisExp.addData('trialnr', thistrials.iloc[trial_num, 0])
        thisExp.addData('trial', thistrials.iloc[trial_num, 1])
        thisExp.addData('Block', thistrials.iloc[trial_num, 2])
        thisExp.addData('Category1', thistrials.iloc[trial_num, 3])
        thisExp.addData('Prototype1', thistrials.iloc[trial_num, 4])
        thisExp.addData('Category2', thistrials.iloc[trial_num, 5])
        thisExp.addData('Prototype2', thistrials.iloc[trial_num, 6])
        thisExp.addData('morphrate1', thistrials.iloc[trial_num, 7])
        thisExp.addData('morphrate2', thistrials.iloc[trial_num, 8])
        thisExp.addData('names', thistrials.iloc[trial_num, 9])
        thisExp.addData('ISI_jitter', str(thisISI_jitter[trial_num]))
        if kb.keys in ['', [], None]:  # No response was made
            kb.keys = None
        thisExp.addData('key',kb.keys)
        
        thisExp.addData('rt', kb.rt)
        
        #save information if sound was sucessfully played in data file
        if thisSound.status == NOT_STARTED:
            play=0
        elif thisSound.status == STARTED:
            play = 1
        elif thisSound.status == FINISHED:
            play = 2
            
        thisExp.addData('play', play)
        thisExp.addData('onset', thistrial_time)
        thisExp.nextEntry()
        trial_num += 1
#---------------------------------------------

#cleanup
thisimage.setAutoDraw(False)
mywin.close()
core.quit()

from keypress import keyPress
import random
import threading
import time
import datetime

# Auto Battle Integration
autoDuration = 15
autoMacroDur = 45
manualOn = 1
manualFirst = 1

# Movement related vars
movementDirection = 1
movementDistMin = 0.6
movementDistMax = 1.2
movementDuration = 0.0
movementCountMin = 6
movementCountMax = 9
movementCount = random.choice(range(movementCountMin,movementCountMax,1))

# Numbers of times to triggers and buttons binded for attacks
# 0 if you wish to trigger a double move

skillRand = [0, 2, 2, 2]
#skillRand = [0, 3, 3, 2, 3]

skillButton = ["skill1"]
skillSlpMin = 0.3
skillSlpMax = 0.5

# Buttons binded for character buff spells

buffEnabled = 1
buffNow = 1
buffWaitMin = 200
buffWaitMax = 220
buffButton = ["skill5","skill4","skill3","skill2"]
buffSlpMin = 0.4
buffSlpMax = 0.9
# For switching to buff
buffButtonSwitch = "toggle"
buffSwitch = 0

# Buttons binded for summon spells
summonEnabled = 0
summonNow = 1
summonWaitMin = 120
summonWaitMax = 220
summonButton = ["skill5"]
summonSlpMin = 0.4
summonSlpMax = 0.9


def toggleAuto():
	global manualOn, manualFirst
	manualOn = not manualOn
	if manualFirst:
		manualOn = not manualOn
	if manualOn:
		if not manualFirst:
			manualOn = 0
			time.sleep(random.uniform(1,1.3))
			keyPress("ab", random.uniform(0.7,1.1))
			time.sleep(random.uniform(0.3,0.7))
			manualOn = 1
		else:
			manualFirst = 0
		threading.Timer(autoMacroDur, toggleAuto).start()
	else:
		manualOn = 0
		time.sleep(random.uniform(0.8,1.1))
		keyPress("ab", random.uniform(0.7,1.1))
		time.sleep(random.uniform(0.9,1.3))
		keyPress("abs", random.uniform(0.7,1.1))
		manualOn = 0
		threading.Timer(autoDuration, toggleAuto).start()

def castSkill():
	if manualOn:
		if buffEnabled:
			if buffNow:
				castBuffNow()
				castBuff()
				rand = random.choice(random.sample(range(buffWaitMin,buffWaitMax),1))
				print ("[" + datetime.datetime.fromtimestamp(time.time()).strftime('%d-%m %H:%M:%S') + "] - " + "'" + str(rand) + "'" + " seconds until next castBuff()")
				threading.Timer(rand, castBuffNow).start()

		if summonEnabled:
			if summonNow:
				castSummonNow()
				castSummon()
				rand = random.choice(random.sample(range(summonWaitMin,summonWaitMax),7))
				print ("[" + datetime.datetime.fromtimestamp(time.time()).strftime('%d-%m %H:%M:%S') + "] - " + "'" + str(rand) + "'" + " seconds until next castSummon()")
				threading.Timer(rand, castSummonNow).start()

		for x in range(random.choice(skillRand)):
			keyPress(random.choice(skillButton), random.uniform(0.1,0.3))
			time.sleep(random.uniform(skillSlpMin,skillSlpMax))

def castBuff():
	if buffSwitch:
		keyPress(buffButtonSwitch, random.uniform(0.1,0.3))
	for keyValue in buffButton:
		keyPress(keyValue, random.uniform(0.1,0.3))
		time.sleep(random.uniform(buffSlpMin,buffSlpMax))
	if buffSwitch:
		keyPress(buffButtonSwitch, random.uniform(0.1,0.3))

def castBuffNow():
	global buffNow
	buffNow = not buffNow

def castSummon():
	for keyValue in summonButton:
		keyPress(keyValue, random.uniform(0.1,0.3))
		time.sleep(random.uniform(summonSlpMin,summonSlpMax))

def castSummonNow():
	global summonNow
	summonNow = not summonNow

def charMove():
	if manualOn:
		global movementDirection, movementDuration, movementCount
		duration = random.uniform(movementDistMin,movementDistMax)
		if movementDirection:
			movementDuration += duration
			keyPress('right', duration)
		else:
			movementDuration -= duration
			keyPress('left', duration)

		if movementCount <= 0:
			if movementDuration > 0:
				keyPress('left', movementDuration)
			else:
				keyPress('right', movementDuration * -1)

			print ("[" + datetime.datetime.fromtimestamp(time.time()).strftime('%d-%m %H:%M:%S') + "] - " + "Zero-ing character to starting point")
			movementCount = random.choice(range(movementCountMin,movementCountMax,1))
			movementDuration = 0.0

		movementDirection = not movementDirection
		movementCount -= 1

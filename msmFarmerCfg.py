from keypress import keyPress
import random
import threading
import time
import datetime

# Movement related vars
movementDirection = 1
movementDuration = 0.0
movementCount = 0
buffNow = 1
summonNow = 1

config_dict = { "shadow":"andy"}

def setConfig(cfg):
	global config_dict, movementCount
	config_dict = cfg
	print(config_dict)
	movementCount = random.choice(range(config_dict["movement"]["stepsMin"],config_dict["movement"]["stepsMax"],1))

def toggleAuto():
	global config_dict
	config_dict["autobattle"]["manualOn"] = not config_dict["autobattle"]["manualOn"]
	if config_dict["autobattle"]["manualFirst"]:
		config_dict["autobattle"]["manualOn"] = not config_dict["autobattle"]["manualOn"]
	if config_dict["autobattle"]["manualOn"]:
		if not config_dict["autobattle"]["manualFirst"]:
			config_dict["autobattle"]["manualOn"] = 0
			time.sleep(random.uniform(1,1.3))
			keyPress("ab", random.uniform(0.7,1.1))
			time.sleep(random.uniform(0.3,0.7))
			config_dict["autobattle"]["manualOn"] = 1
		else:
			config_dict["autobattle"]["manualFirst"] = 0
		threading.Timer(config_dict["autobattle"]["durManual"], toggleAuto).start()
	else:
		config_dict["autobattle"]["manualOn"] = 0
		time.sleep(random.uniform(0.8,1.1))
		keyPress("ab", random.uniform(0.7,1.1))
		time.sleep(random.uniform(0.9,1.3))
		keyPress("abs", random.uniform(0.7,1.1))
		config_dict["autobattle"]["manualOn"] = 0
		threading.Timer(config_dict["autobattle"]["durAuto"], toggleAuto).start()

def castSkill():
	if config_dict["autobattle"]["manualOn"]:
		if config_dict["buffs"]["enabled"]:
			if buffNow:
				castBuffNow()
				castBuff()
				rand = random.choice(random.sample(range(config_dict["buffs"]["cdMin"],config_dict["buffs"]["cdMax"]),1))
				print ("[" + datetime.datetime.fromtimestamp(time.time()).strftime('%d-%m %H:%M:%S') + "] - " + "'" + str(rand) + "'" + " seconds until next castBuff()")
				threading.Timer(rand, castBuffNow).start()
		if config_dict["summons"]["enabled"]:
			if summonNow:
				castSummonNow()
				castSummon()
				rand = random.choice(random.sample(range(config_dict["summons"]["cdMin"],config_dict["summons"]["cdMax"]),7))
				print ("[" + datetime.datetime.fromtimestamp(time.time()).strftime('%d-%m %H:%M:%S') + "] - " + "'" + str(rand) + "'" + " seconds until next castSummon()")
				threading.Timer(rand, castSummonNow).start()
		for x in range(random.choice(config_dict["skills"]["distribution"])):
			keyPress(random.choice(config_dict["skills"]["buttons"]), random.uniform(0.1,0.3))
			time.sleep(random.uniform(config_dict["skills"]["waitMin"],config_dict["skills"]["waitMax"]))

def castBuff():
	if config_dict["buffs"]["toggleNeeded"]:
		keyPress(config_dict["buffs"]["toggleButton"], random.uniform(0.1,0.3))
	for keyValue in config_dict["buffs"]["buttons"]:
		keyPress(keyValue, random.uniform(0.1,0.3))
		time.sleep(random.uniform(config_dict["buffs"]["waitMin"],config_dict["buffs"]["waitMax"]))
	if config_dict["buffs"]["toggleNeeded"]:
		keyPress(config_dict["buffs"]["toggleButton"], random.uniform(0.1,0.3))

def castBuffNow():
	global buffNow
	buffNow = not buffNow

def castSummon():
	for keyValue in config_dict["summons"]["buttons"]:
		keyPress(keyValue, random.uniform(0.1,0.3))
		time.sleep(random.uniform(config_dict["summons"]["waitMin"],config_dict["summons"]["waitMax"]))

def castSummonNow():
	global summonNow
	summonNow = not summonNow

def charMove():
	if config_dict["autobattle"]["manualOn"]:
		global movementDirection, movementDuration, movementCount
		duration = random.uniform(config_dict["movement"]["distMin"],config_dict["movement"]["distMax"])
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
			movementCount = random.choice(range(config_dict["movement"]["distMin"],config_dict["movement"]["distMax"],1))
			movementDuration = 0.0

		movementDirection = not movementDirection
		movementCount -= 1

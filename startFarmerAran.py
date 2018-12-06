from msmFarmerCfg import setConfig, charMove, castSkill, toggleAuto
import time
import random
import json

config = """{
	"device": {
		"host": "127.0.0.1",
		"port": 5037,
		"name": "emulator-5554"
	},
	"autobattle": {
		"durAuto": 15,
		"durManual": 60,
		"manualOn": 1,
		"manualFirst": 1
	},
	"movement": {
		"distMin": 0.2,
		"distMax": 0.6,
		"stepsMin": 6,
		"stepsMax": 9
	},
	"skills": {
		"distribution": [0, 2, 2, 2],
		"buttons": ["skill1"],
		"waitMin": 0.3,
		"waitMax": 0.5
	},
	"buffs": {
		"enabled": 1,
		"buttons": ["skill2", "skill3"],
		"cdMin": 20,
		"cdMax": 35,
		"waitMin": 0.4,
		"waitMax": 0.9,
		"toggleNeeded": 0,
		"toggleButton": "toggle"
	},
	"summons": {
		"enabled": 1,
		"buttons": ["skill3", "skill4"],
		"cdMin": 120,
		"cdMax": 240,
		"waitMin": 0.4,
		"waitMax": 0.9
	}
}"""

config_dict = json.loads(config)
#print config_dict
#print random.choice(range(config_dict["movement"]["stepsMin"],config_dict["movement"]["stepsMax"],1))

# Allowing time to toggle to BlueStacks
time.sleep(2.5)
setConfig(config_dict)
toggleAuto()

# Looping through farming
while True:
	castSkill()
	time.sleep(random.uniform(0.2,0.4))
	charMove()
	time.sleep(random.uniform(0.3,0.5))

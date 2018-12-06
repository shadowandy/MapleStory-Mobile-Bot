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
		"durAuto": 60,
		"durManual": 30,
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
		"distribution": [3],
		"buttons": ["skill1", "skill2"],
		"waitMin": 0.1,
		"waitMax": 0.3
	},
	"buffs": {
		"enabled": 1,
		"buttons": ["skill3", "skill4", "skill2", "skill5", "skill1"],
		"cdMin": 180,
		"cdMax": 240,
		"waitMin": 0.4,
		"waitMax": 0.9,
		"toggleNeeded": 1,
		"toggleButton": "toggle"
	},
	"summons": {
		"enabled": 0,
		"buttons": ["skill3", "skill4", "skill2", "skill5"],
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

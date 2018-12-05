from msmFarmerCfg import setConfig, charMove, castSkill, toggleAuto
import time
import random
import json

config = """{
	"autobattle": {
		"durAuto": 5,
		"durManual": 10,
		"manualOn": 1,
		"manualFirst": 1
	},
	"movement": {
		"distMin": 0.2,
		"distMax": 0.6,
		"stepsMin": 2,
		"stepsMax": 3
	},
	"skills": {
		"distribution": [1, 1],
		"buttons": ["skill1"],
		"waitMin": 0.3,
		"waitMax": 0.5
	},
	"buffs": {
		"enabled": 1,
		"buttons": ["skill4", "skill3"],
		"cdMin": 45,
		"cdMax": 60,
		"waitMin": 0.4,
		"waitMax": 0.9,
		"toggleNeeded": 0,
		"toggleButton": "toggle"
	},
	"summons": {
		"enabled": 1,
		"buttons": ["skill5"],
		"cdMin": 250,
		"cdMax": 290,
		"waitMin": 0.4,
		"waitMax": 0.9
	}
}"""

config_dict = json.loads(config)

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

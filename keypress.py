from adb.client import Client as AdbClient
import time
import random
import datetime
# for image recognition
import cv2
import numpy as np

# Connecting to BlueStacks
# Requires ./adb start-server; ./adb devices to be done prior
#client = AdbClient(host="127.0.0.1", port=5037)
#device = client.device("emulator-5554")

def encounteredreCAPTCHA():
	template = cv2.imread('image/recaptcha.png',0)
	result = device.screencap()
	npimg = np.fromstring(str(result), np.uint8)
	img = cv2.imdecode(npimg,0)
	res = cv2.matchTemplate(img,template,'cv2.TM_CCOEFF')
	threshold = 0.8
	flag = False
	for i in res:
	    if i.any() > threshold:
	        flag = True
	return flag

def keyPress(device, keyValue, duration):
	dur = int(duration * 1000)
	loc = [0,0]

	if keyValue == "left":
		loc = [100,800]
	elif keyValue == "right":
		loc = [350,800]
	elif keyValue == "up":
		loc = [220,675]
	elif keyValue == "down":
		loc = [220,900]
	elif keyValue == "skill1":
		loc = [1650,900]
	elif keyValue == "skill2":
		loc = [1450,955]
	elif keyValue == "skill3":
		loc = [1450,820]
	elif keyValue == "skill4":
		loc = [1560,710]
	elif keyValue == "skill5":
		loc = [1715,700]
	elif keyValue == "ab":
		loc = [520,950]
	elif keyValue == "abs":
		loc = [930,800]
	elif keyValue == "toggle":
		loc = [1850,705]
	elif keyValue == "jump":
		loc = [1835,880]
	else:
		loc = [500,900]
	device.shell("input swipe " + str(loc[0]) + " " + str(loc[1]) + " " + str(loc[0]) + " " + str(loc[1]) + " " + str(dur))
	print ("[" + datetime.datetime.fromtimestamp(time.time()).strftime('%d-%m %H:%M:%S') + "] - " + "'" + keyValue + "'" + " key pressed!")
	time.sleep(random.uniform(0.1,0.2))

def mouseClick(xi,yi):
	dur = int(random.uniform(0.4,0.7) * 1000)
	dx = 800
	dy = 800
	device.shell("input swipe " + str(dx) + " " + str(dy) + " " + str(dx) + " " + str(dy) + " " + str(dur))
	print ("Mouse clicked!")

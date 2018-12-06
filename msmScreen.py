from adb.client import Client as AdbClient
import cv2
import numpy as np

client = AdbClient(host="127.0.0.1", port=5037)
device = client.device("emulator-5554")

def recaptchaFound():
	template = cv2.imread('images/recaptcha.png',0)
	result = device.screencap()
	npimg = np.fromstring(str(result), np.uint8)
	img = cv2.imdecode(npimg,0)
	res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF)
	threshold = 0.8
	flag = False
	for i in res:
	    if i.any() > threshold:
	        flag = True
	return flag

print(str(recaptchaFound()))

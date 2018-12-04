from adb.client import Client as AdbClient
import time
import random
import datetime
# for image recognition
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Connecting to BlueStacks
# Requires ./adb start-server; ./adb devices to be done prior
client = AdbClient(host="127.0.0.1", port=5037)
device = client.device("emulator-5554")

def encounteredreCAPTCHA():
	#template = cv2.imread('recaptcha.png',0)
	template = cv2.imread('images/recaptcha.png',0)
	w, h = template.shape[::-1]
	result = device.screencap()
	#with open("screen.png", "wb") as fp:
	#	fp.write(result)
	npimg = np.fromstring(str(result), np.uint8)
	img = cv2.imdecode(npimg,0)
	#img = cv2.imread('screen.png',0)
	sift = cv2.xfeatures2d.SIFT_create()

	# find the keypoints and descriptors with SIFT
	kp1, des1 = sift.detectAndCompute(template,None)
	kp2, des2 = sift.detectAndCompute(img,None)

	# BFMatcher with default params
	bf = cv2.BFMatcher()
	matches = bf.knnMatch(des1,des2, k=2)

	# Apply ratio test
	good = []
	for m,n in matches:
		if m.distance < 0.75*n.distance:
			good.append([m])

	# cv2.drawMatchesKnn expects list of lists as matches.
	img3 = cv2.drawMatchesKnn(template,kp1,img,kp2,good,flags=2,outImg=None)

	plt.imshow(img3),plt.show()
	#threshold = 0.9
	#flag = False
	#for i in res:
	#    if i.any() > threshold:
	#        flag = True
	#return flag

#print("reCaptcha Seen: " + str(encounteredreCAPTCHA()))
encounteredreCAPTCHA()

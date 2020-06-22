import cv2
import time
import numpy as np
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

tmp = -1
cred = credentials.Certificate('lab411-a9813-firebase-adminsdk-zhpav-469b199d3c.json')
firebase_admin.initialize_app(cred, {
    			'storageBucket': 'lab411-a9813.appspot.com'
				})
while True:
	tm = time.localtime(time.time())
	if (tm[5] != tmp) and (tm[5] % 10 == 0):
		#rtsp_domain = "rtsp://admin:88888888abc@192.168.0.102:554/Streaming/Channels/101"
		#rtsp_domain = "rtsp://192.169.0.100:554/onvif1"
		cap = cv2.VideoCapture(1)
		tmp = tm[5]
		print("capture")
		if cap.isOpened():
			ret, frame = cap.read()
			if ret:
				t = time.asctime(tm)
				filename = 'images/'+str(t) +'.jpg' 
				cv2.imwrite(filename,frame)

				bucket = storage.bucket()

				blob = bucket.blob(filename)
				blob.upload_from_filename(filename)

				print(blob.self_link)
		cap.release()


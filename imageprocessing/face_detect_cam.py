import cv2
import numpy as np
import time
from time import sleep
import post_to_webservice

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = []

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    if len(faces) > 0:
        all_face_snips = []
        for (x, y, w, h) in faces:
            snip_face = frame[y-5:y+h+5,x-5:x+w+5]
            all_face_snips.append(snip_face)
            print("Faces detected: " + str(len(all_face_snips)))
        for i in range(len(all_face_snips)):
            #np.save("detected-faces/face" + time.strftime("%Y%m%d-%H%M%S") + ".npy", all_face_snips[i])
            cv2.imwrite("detected-faces/face" + time.strftime("%Y%m%d-%H%M%S") + ".png", all_face_snips[i])       
        post_to_webservice.send_request()
        sleep(5)
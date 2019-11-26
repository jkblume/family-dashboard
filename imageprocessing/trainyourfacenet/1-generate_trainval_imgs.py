import cv2
import numpy as np
import time
from PIL import Image
from numpy import asarray
from mtcnn import MTCNN
import os

target_folder_name = "Jule" # name for folder structure
target_folder_data = "val" # val or train

# make directory for new names // train and val need to be in sync
PROJECT_ROOT_DIR = "."
IMAGES_PATH = os.path.join(PROJECT_ROOT_DIR, "yourfamfortraining/" + target_folder_data + "/" + target_folder_name)
os.makedirs(IMAGES_PATH, exist_ok=True)

#extract one face from frame (or image in test scenario)
def extract_face(image,required_size=(160,160)):
    #initialize Face Net implementation
    detector=MTCNN()
    #detect all faces
    results=detector.detect_faces(image)
    for i in range(len(results)):
        print(results[i]['confidence'])
        #only above 95% confidence
        if results[i]['confidence'] > 0.9:
            #extracttheboundingboxfromthefirstface
            x1,y1,width,height=results[i]['box']
            #bug fix (sometimes negative vals are returened)
            x1,y1=abs(x1),abs(y1)
            x2,y2=x1+width,y1+height
            #extract the face
            face=image[y1:y2,x1:x2]
            #resize pixels to the model size later used for classification
            image=Image.fromarray(face)
            image=image.resize(required_size)
    return image

video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    face_image = extract_face(frame)
    try:
        face_image.save("yourfamfortraining/" + target_folder_data + "/" + target_folder_name + "/" + time.strftime("%Y%m%d-%H%M%S") + ".png")
        print("Face Image Saved")
    except:
        #print("error when saving, trying to go on")
        #print(type(face_image))
        pass
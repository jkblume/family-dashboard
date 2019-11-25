import cv2
import numpy as np
from numpy import load
from numpy import expand_dims
from numpy import asarray
from time import sleep
from PIL import Image
from numpy import asarray
from mtcnn import MTCNN
from joblib import load
import tensorflow
from sklearn.preprocessing import Normalizer
from sklearn.svm import SVC

#extract all faces from frame (or image in test scenario)
def extract_face(image,required_size=(160,160)):
    #initialize Face Net implementation
    detector=MTCNN()
    #detect all faces
    results=detector.detect_faces(image)
    #create two lists to store faces per run
    all_faces_array=[]
    all_imgs_array=[]
    for i in range(len(results)):
        print(results[i]['confidence'])
        #only above 95% confidence
        if results[i]['confidence'] > 0.95:
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
            face_array=asarray(image)
            all_faces_array.append(face_array)
            all_imgs_array.append(image)
    return all_faces_array,all_imgs_array

def get_embedding(model, face_pixels):
	# scale pixel values
	face_pixels = face_pixels.astype('float32')
	# standardize pixel values across channels (global)
	mean, std = face_pixels.mean(), face_pixels.std()
	face_pixels = (face_pixels - mean) / std
	# transform face into one sample
	samples = expand_dims(face_pixels, axis=0)
	# make prediction to get embedding
	predicted_embedding = model.predict(samples)
	return predicted_embedding

# start webcam
video_capture = cv2.VideoCapture(0)
# load SVM and tf facenet model
clf = load('trainyourfacenet/svm-clf-model.joblib')
embedding_model = tensorflow.keras.models.load_model('trainyourfacenet/facenet_keras.h5')

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    face_arrays, face_images = extract_face(frame)
    # get the embedding vector
    face_embeddings = []
    # get the embedding vector of all detected faces
    for i in range(len(pixels[0])):
        face_embedding = get_embedding(embedding_model, pixels[0][i])
        # normalize input vectors
        in_encoder = Normalizer(norm='l2')
        face_embedding = in_encoder.transform(face_embedding)
        print(face_embedding.shape)
        face_embeddings.append(face_embedding)
    # predict
    face_embeddings = asarray(face_embeddings)
    print(face_embeddings.shape)
    face_embeddings = np.squeeze(face_embeddings)
    print(face_embeddings.shape)

    predicted_classes = clf.predict(face_embeddings)
    predicted_probas = clf.predict_proba(face_embeddings)

    # summarize
    print("Klasse:")
    print(predicted_classes)
    print("Konfidenz:")
    print(predicted_probas)

    sleep(5)
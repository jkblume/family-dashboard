import requests
import os

def download_model():
	url='https://jundm-fam-dashboard-bucket.s3.eu-de.cloud-object-storage.appdomain.cloud/facenet_keras.h5'
	filename = 'facenet_keras.h5'

	if not os.path.exists(filename):
		r = requests.get(url)
		with open('facenet_keras.h5', 'wb') as f:
			f.write(r.content)
		print("File downloaded")
	else:
		print("error or it exists already")



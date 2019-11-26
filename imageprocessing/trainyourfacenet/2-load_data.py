from os import listdir
from os.path import isdir
from numpy import asarray
from PIL import Image
from numpy import savez_compressed

# load images and extract faces for all images from a directory
def load_faces(directory):
	faces = list()
	# enumerate files
	for filename in listdir(directory):
		# path
		path = directory + filename
		# get face
		image = Image.open(path)
		# convert to array
		img_array = asarray(image)
		# store
		faces.append(img_array)
	return faces

# load a dataset that contains one subdir for each class that in turn contains images
def load_dataset(directory):
	X, y = list(), list()
	# enumerate folders, on per class
	for subdir in listdir(directory):
		# path
		path = directory + subdir + '/'
		# skip any files that might be in the dir
		if not isdir(path):
			continue
		# load all faces in the subdirectory
		faces = load_faces(path)
		# create labels
		labels = [subdir for _ in range(len(faces))]
		# summarize progress
		print('>loaded %d examples for class: %s' % (len(faces), subdir))
		# store
		X.extend(faces)
		y.extend(labels)
	return asarray(X), asarray(y)

# load train dataset
trainX, trainy = load_dataset('yourfamfortraining/train/')
print(trainX.shape, trainy.shape)
# load test dataset
testX, testy = load_dataset('yourfamfortraining/val/')
print(testX.shape, testy.shape)
# save arrays to one file in compressed format
savez_compressed('family-dataset.npz', trainX, trainy, testX, testy)
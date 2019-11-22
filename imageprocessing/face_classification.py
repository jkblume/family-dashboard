import numpy as np
from os import listdir
from os.path import isfile, join
import tensorflow
from PIL import Image


all_images = [f for f in listdir("detected-faces") if isfile(join("detected-faces", f))]

#array1 = np.load("detected-faces/" + onlyfiles[0])

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = tensorflow.keras.models.load_model('tf-model/keras_model.h5')

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Replace this with the path to your image
image = Image.open("detected-faces/" + all_images[len(all_images)-1])

# Make sure to resize all images to 224, 224 otherwise they won't fit in the array
image = image.resize((224, 224))
image_array = np.asarray(image)
print(image_array.shape)

# Normalize the image
normalized_image_array = image_array / 255.0

# Load the image into the array
data[0] = normalized_image_array

# run the inference
prediction = model.predict(data)
print(prediction)
class_index = np.where(prediction == np.amax(prediction))[1][0]

# link prediction to label
f=open("tf-model/labels.txt", "r")
contents=f.readlines()
f.close()

final_labels = []
for i in range(len(contents)):
    split_line = contents[i].split(" ")
    final_labels.append(split_line)

print(final_labels[class_index][1])



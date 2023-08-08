from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.utils import to_categorical, plot_model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import BatchNormalization, Conv2D, MaxPooling2D, Activation, Flatten, Dropout, Dense
from tensorflow.keras import backend as K
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
import random
import cv2
import os
import glob

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# initial parameters
epochs = 10
lr = 1e-3
batch_size = 64
img_dims = (96,96,3)

data = []
labels = []
print("Successful Initial parameters\n")

# load image files from the dataset
image_files = [f for f in glob.glob(r'C:/Users/Dell/OneDrive/Desktop/KUSHAL/python/College/dataset' + "/**/*", recursive=True) if not os.path.isdir(f)]
random.shuffle(image_files)
print("Successful Load image\n")

# converting images to arrays and labelling the categories
for img in image_files:

    image = cv2.imread(img)
    
    image = cv2.resize(image, (img_dims[0],img_dims[1]))
    image = img_to_array(image)
    data.append(image)

    label = img.split(os.path.sep)[-2] # C:\Files\gender_dataset_face\woman\face_1162.jpg
    if label == "woman":
        label = 1
    else:
        label = 0
        
    labels.append([label]) # [[1], [0], [0], ...]

print("Successful converting image to arrays\n")

# pre-processing
data = np.array(data, dtype="float") / 255.0
labels = np.array(labels)

#print("Data: ", data)
#print("Labels: ", labels)
print("Successful Pre-processing\n")

# split dataset for training and validation
trainX, testX, trainY, testY = train_test_split(data, labels, test_size=0.2, random_state=42)

trainY = to_categorical(trainY, num_classes=2) # [[1, 0], [0, 1], [0, 1], ...]
testY = to_categorical(testY, num_classes=2)
print("Successful Split\n")

# augmenting datset 
aug = ImageDataGenerator(rotation_range=25, width_shift_range=0.1,
    height_shift_range=0.1, shear_range=0.2, zoom_range=0.2,
    horizontal_flip=True, fill_mode="nearest"
)
print("Successful Aug dataset\n")



# define model
def build(width, height, depth, classes):
    model = Sequential()
    inputShape = (height, width, depth)
    chanDim = -1

    if K.image_data_format() == "channels_first": #Returns a string, either 'channels_first' or 'channels_last'
        inputShape = (depth, height, width)
        chanDim = 1
    
    # The axis that should be normalized, after a Conv2D layer with data_format="channels_first", 
    # set axis=1 in BatchNormalization.

    model.add(Conv2D(32, (3,3), padding="same", input_shape=inputShape))
    model.add(Activation("relu"))
    model.add(BatchNormalization(axis=chanDim))
    model.add(MaxPooling2D(pool_size=(3,3)))
    model.add(Dropout(0.25))

    model.add(Conv2D(64, (3,3), padding="same"))
    model.add(Activation("relu"))
    model.add(BatchNormalization(axis=chanDim))

    model.add(Conv2D(64, (3,3), padding="same"))
    model.add(Activation("relu"))
    model.add(BatchNormalization(axis=chanDim))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.25))

    model.add(Conv2D(128, (3,3), padding="same"))
    model.add(Activation("relu"))
    model.add(BatchNormalization(axis=chanDim))

    model.add(Conv2D(128, (3,3), padding="same"))
    model.add(Activation("relu"))
    model.add(BatchNormalization(axis=chanDim))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.25))

    model.add(Flatten())
    model.add(Dense(1024))
    model.add(Activation("relu"))
    model.add(BatchNormalization())
    model.add(Dropout(0.5))

    model.add(Dense(classes))
    model.add(Activation("sigmoid"))

    return model


print("Successful define model\n")

# build model
model = build(width=img_dims[0], height=img_dims[1], depth=img_dims[2],
                            classes=2)

print("Successful build model\n")


# compile the model
opt = Adam(learning_rate=lr, decay=lr/epochs)
model.compile(loss="binary_crossentropy", optimizer=opt, metrics=["accuracy"])
print("Successful compile model\n")


# train the model
H = model.fit(trainX, trainY, epochs=epochs, validation_data=(testX, testY))

print("Successful train model\n")

# save the model to disk
model.save('gender_detection.model')
print("Successful save model\n")

# plot training/validation loss/accuracy
plt.style.use("ggplot")
plt.figure()
N = 3

print("H.history: ", H.history)
plt.plot(np.arange(0,len(H.history["loss"])), H.history["loss"], label="Loss")
plt.plot(H.history["accuracy"], label="Accuracy")
plt.plot(H.history["val_accuracy"], label="Validation Accuracy")
plt.plot(H.history["val_loss"], label="Validation Loss")

plt.title("Training Loss and Accuracy")
plt.xlabel("Epoch #")
plt.ylabel("Loss/Accuracy")
plt.legend(loc="upper right")

# save plot to disk
plt.savefig('plot_with_aug.png')

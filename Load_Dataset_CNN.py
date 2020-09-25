import tensorflow as tf
import cv2
import os
import pickle
import numpy as np

# making variables that will be used throughout
image_data = []
x_data = []
y_data = []
CATEGORIES = []

IMAGE_SIZE = 300

DIREC_PATH = "/Users/raveena/Desktop/Training_Example/train"

# this will go through the directory given and list the folders within
def get_categories():
    list_categories = []  # keep tracks of the list of categories
    for folder in os.listdir(DIREC_PATH):
        if ".DS_Store" in folder:
            pass
        else:
            list_categories.append(folder)
    return list_categories


# This will return numpy arrays of image (X_data, Y_data)
def get_numpy_array(path):
    try:
        CATEGORIES = get_categories()
        for category in CATEGORIES:
            train_folder = os.path.join(DIREC_PATH, category)  # Join one or more path with directory
            class_index = CATEGORIES.index(category)  # This will get the index for classification

            # now go through images in folder
            for img in os.listdir(train_folder):
                img_path = os.path.join(train_folder, img)

                # check if the image is corrupted
                try:
                    image_data_temp = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
                    image_temp_resize = cv2.resize(image_data_temp, (IMAGE_SIZE, IMAGE_SIZE))
                    image_data.append([image_temp_resize, class_index])
                except:
                    print("Corruption" + img_path)
                    pass

            # making into np array
            data = np.asanyarray(image_data, dtype=object)

            # go through data
            for x in data:
                x_data.append(x[0])  # get the X_Data
                x_data.append(x[1])  # get the label

            X_Data = np.asarray(x_data, dtype=object) / (255.0)  # normalize data
            Y_Data = np.asarray(y_data, dtype=object)

            # reshape x_data
            X_Data = X_Data.reshape(-1, IMAGE_SIZE, IMAGE_SIZE, 1)

            return X_Data, Y_Data

    except:
        print("Failed to run Function Process Image")

# Creates a pickle object of Dataset
def pickle_image():
    X_Data, Y_Data = get_numpy_array(DIREC_PATH)

    # write the entire data into a pickle file
    pickle_out = open('X_Data', 'wb')
    pickle.dump(X_Data, pickle_out)
    pickle_out.close()

    # write the Y Label Data
    pickle_out = open('Y_Data', 'wb')
    pickle.dump(Y_Data, pickle_out)
    pickle_out.close()

    print("Pickled Image Successfully")
    return X_Data, Y_Data


def load_dataset():
    try:
        # Read data from Pickle Object
        X_temp = open('X_Data', 'rb')
        X_Data = pickle.load(X_temp)

        Y_temp = open('Y_Data', 'rb')
        Y_Data = pickle.load(Y_temp)

        print("Reading dataset from pickle object")

        return X_Data, Y_Data

    except:
        print('Could not find pickle file')
        print("loading file and dataset....")

        X_Data, Y_Data = pickle_image()
        return X_Data, Y_Data

if __name__ == '__main__':
    X_Data, Y_Data = load_dataset()
    print(X_Data.shape)
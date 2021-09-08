import numpy as np
import cv2
import time
import os

from utils.grabscreen import grab_screen
from utils.getkeys import key_check

file_name = "Datas/training_data.npy"
file_name2 = "Datas/target_data.npy"


w = [1, 0, 0, 0, 0]
a = [0, 1, 0, 0, 0]
s = [0, 0, 1, 0, 0]
d = [0, 0, 0, 1, 0]

space = [0,0,0,0,1]


def keys_to_output(keys):

    output = [0, 0, 0, 0, 0]

    if 'W' in keys:
        output = w
    elif 'A' in keys:
        output = a
    elif 'S' in keys:
        output = s
    elif 'D' in keys:
        output = d
    elif " " in keys:
        output= space
    return output

def get_data():

    if os.path.isfile(file_name):
        print('File exists, loading previous data!')
        image_data = list(np.load(file_name, allow_pickle=True))
        targets = list(np.load(file_name2, allow_pickle=True))
    else:
        print('File does not exist, starting fresh!')
        image_data = []
        targets = []
    return image_data, targets


def save_data(image_data, targets):
    np.save(file_name, image_data)
    np.save(file_name2, targets)


image_data, targets = get_data()
while True:
    keys = key_check()
    print("waiting press B to start")
    if keys == "B":
        print("Starting")
        break

count = 0
while True:
    count +=1
    last_time = time.time()
    image = grab_screen(region=(50, 130, 500, 520))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    image = cv2.Canny(image, threshold1=200, threshold2=400)

    image = cv2.resize(image, (84, 84))

    cv2.imshow("AI Peak", image)
    cv2.waitKey(1)

    image = np.array(image)
    image_data.append(image)
    output = keys_to_output(keys)
    keys = key_check()
    targets.append(keys)
    if keys == "H":
        cv2.destroyAllWindows() 
        break
    
    tim = time.time()-last_time
    print(1/tim)
    print(output)
    print(keys)

save_data(image_data, targets)

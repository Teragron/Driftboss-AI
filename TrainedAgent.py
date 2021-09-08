import random
import time

from utils.getkeys import key_check
import keyboard
import time
import cv2
from utils.grabscreen import grab_screen
from utils.directkeys import PressKey, ReleaseKey, W, D, A
from fastai.vision.all import *                 
import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

def label_func(x): return x.parent.name
learn_inf = load_learner("Models/178k.pkl")
print("loaded learner")


sleepy = 0.1

keyboard.wait('B')
time.sleep(sleepy)


while True:

    image = grab_screen(region=(50, 130, 500, 520))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.Canny(image, threshold1=200, threshold2=400)
    image = cv2.resize(image,(84,84))

    start_time = time.time()
    result = learn_inf.predict(image)
    action = result[0]

    
    if action == "Space":
        keyboard.press("space")
        print(action)

    elif action == "Nothing":
        keyboard.release("space")
        print(action)

    keys = key_check()
    if keys == "H":
        break

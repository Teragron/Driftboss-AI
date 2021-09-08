import cv2
import numpy as np

data = np.load("Datas/training_data.npy", allow_pickle=True)
targets = np.load("Datas/target_data.npy", allow_pickle=True)

print(f'Image Data Shape: {data.shape}')
print(f'targets Shape: {targets.shape}')


unique_elements, counts = np.unique(targets, return_counts=True)
print(np.asarray((unique_elements, counts)))


holder_list = []
for i, image in enumerate(data):
    holder_list.append([data[i], targets[i]])


count_space = 0
count_n = 0


for data in holder_list:

    if data[1] == " ":
        count_space += 1
        cv2.imwrite(f"Space/H4-j{count_space}.png", data[0])
    elif data[1] == ".":
        count_n += 1
        cv2.imwrite(f"Nothing/H4-j{count_n}.png", data[0]) 

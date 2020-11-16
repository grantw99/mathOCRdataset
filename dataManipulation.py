import os
import cv2
import numpy as np
import random

def randResize(cv2_in, new_path):
    blank_image = np.zeros((45, 45, 3), np.uint8)
    blank_image[:,0:45] = (255,255,255)

    new_dim = random.randint(30, 45)

    resized = cv2.resize(cv2_in, (new_dim, new_dim))
    h1, w1 = resized.shape[:2]
    h2, w2 = blank_image.shape[:2]

    pip_h = (h2-h1)//2
    pip_w = (w2-w1)//2

    blank_image[pip_h:pip_h+h1, pip_w:pip_w+w1] = resized

    print("Write new image to: {}".format(new_path))
    cv2.imwrite(new_path, blank_image)

all_dir = './all_imgs'
for tt in os.listdir(all_dir):
    for class_folder in os.listdir("{}/{}".format(all_dir, tt)):
        for img in os.listdir("{}/{}/{}".format(all_dir, tt, class_folder)):
            im_path = "{}/{}/{}/{}".format(all_dir, tt, class_folder, img)
            resized_path = "{}/{}/{}/{}".format(all_dir, tt, class_folder, "_resized.".join(img.split('.')))
            im_in = cv2.imread(im_path)
            randResize(im_in, resized_path)

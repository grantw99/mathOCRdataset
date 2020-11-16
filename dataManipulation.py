import os
import cv2
import numpy as np
import random
import math
import imutils

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
    cv2.imwrite("./new.jpg", blank_image)

def randRotate(cv2_in, new_path):
    degs = random.randint(-15,15)
    print(degs)
    new_angle = math.radians(degs)
    new_size = abs(int((45*45)//(math.sin(new_angle)*45-math.cos(new_angle)*45)))
    cv2.resize(cv2_in, (new_size, new_size))
    rotated = imutils.rotate_bound(cv2_in, new_angle)

    blank_image = np.zeros((45, 45, 3), np.uint8)
    blank_image[:,0:45] = (255, 255, 255)

    blank_image[:,:] = rotated

    cv2.imshow("image", blank_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

randRotate(cv2.imread('./all_imgs/train/A/17_a_137.jpg'), './new.jpg')
"""
all_dir = './all_imgs'
for tt in os.listdir(all_dir):
    for class_folder in os.listdir("{}/{}".format(all_dir, tt)):
        for img in os.listdir("{}/{}/{}".format(all_dir, tt, class_folder)):
            im_path = "{}/{}/{}/{}".format(all_dir, tt, class_folder, img)
            resized_path = "{}/{}/{}/{}".format(all_dir, tt, class_folder, "_resized.".join(img.split('.')))
            im_in = cv2.imread(im_path)
            randResize(im_in, resized_path)
"""

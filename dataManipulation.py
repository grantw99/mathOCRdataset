import os
import cv2
import numpy as np
import random
import csv
import filecmp
import itertools
import math

def resizeFilePath(path):
    im = cv2.imread(path)
    cv2.resize(im, (32, 32))
    cv2.imwrite(path, im)

def listAllFiles():
    all_files = []
    for root, dirs, files in os.walk('./all_imgs'):
        for name in files:
            all_files.append("{}/{}".format(root.replace('\\', '/'), name))
    return all_files

def resizeAllFiles():
    for im in listAllFiles():
        resizeFilePath(im)

def moveFiles():
    label_table = {}
    file_table = {}
    count_table = {}
    train_nums = {}
    train_to_move = []
    test_to_move = []
    with open('./symbols.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if(row[1] == 'latex'):
                pass
            else:
                label_table[row[0]] = row[1]
    with open('./hasy-data-labels.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if(row[1] in label_table):
                if(label_table[row[1]] in count_table):
                    count_table[label_table[row[1]]] += 1
                else:
                    count_table[label_table[row[1]]] = 1
                file_table[row[0]] = label_table[row[1]]
    for label in count_table:
        train_nums[label] = int((count_table[label]*.8)//1)
    for f in file_table:
        if train_nums[file_table[f]] >= 0:
            train_nums[file_table[f]] -= 1
            train_to_move.append({"src":f, "dest":"./all_imgs/train/{}/{}".format(file_table[f], f.split('/')[-1])})
        else:
            test_to_move.append({"src":f, "dest":"./all_imgs/test/{}/{}".format(file_table[f], f.split('/')[-1])})
    for img in train_to_move:
        os.rename(img['src'], img['dest'])
    for img in test_to_move:
        os.rename(img['src'], img['dest'])

def getNonUniqueFiles(directory):
    dups = []
    directory_files = os.listdir(directory)
    to_search = itertools.combinations(os.listdir(directory), 2)
    to_compare = (math.factorial(len(directory_files)))/(math.factorial(2)*math.factorial(len(directory_files)-2))
    non_unique = []
    template_dir = "{}/{}"
    x = 0
    for f in to_search:
        if (filecmp.cmp(template_dir.format(directory, f[0]), template_dir.format(directory, f[1]))):
            non_unique.append("{}/{}".format(directory, f[0]))
        if (x%10000) == 0: 
            print("{:.2f}% complete in {}".format(x/to_compare, directory))
        x += 1
    return(non_unique)

def getAllNonUniqueFiles():
    tt = os.listdir("./all_imgs")
    non_unique = []
    for folder in tt:
        for sub_folder in os.listdir("./all_imgs/{}".format(folder)):
            print("Scanning {}/{}".format(folder, sub_folder))
            temp = getNonUniqueFiles("./all_imgs/{}/{}".format(folder, sub_folder))
            print("Deleting files: {}".format(temp))
            delFilesInList(temp)
    return non_unique

def delFilesInList(to_delete):
    for f in to_delete:
        os.remove(f)        

delFilesInList(getAllNonUniqueFiles())
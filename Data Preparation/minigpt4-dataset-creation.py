'''
This file is to prepare our dataset folder in the format of MiniGPT-4 image descriptions
'''

import os
import shutil


def tranfer(foodcap500_train_dir, dst_dir):
    for subdir, dirs, files in os.walk(foodcap500_train_dir):
        for file in files:
            try:
                shutil.copy(os.path.join(subdir, file), dst_dir)
            except:
                print(file)



folder  =  "C:/Users/shrey/Downloads/dataset/Final/minigpt4/images"
foodcap500_train_dir = "C:/Users/shrey/Downloads/dataset/Final/ISIA_Food500/ISIA_Food500/data_with_caps/train"
train_file = "C:/Users/shrey/Downloads/dataset/Final/ISIA_Food500/ISIA_Food500/retrieval_dict/metadata_train.csv"
tranfer(foodcap500_train_dir, folder)
'''
This is the file to transfer images from the ISIA_Food500 dataset to the the FoodCap500 dataset 
as the Foodcap500 dataset only have the .json file wiht filename, category and caption.
'''

import os
import re
import shutil


def tranfer(file, copy_dir, folder):
    if(not os.path.exists(copy_dir)):
        os.mkdir(copy_dir, mode = 0o777)
    count = 0
    with open (file,'r',encoding="utf8") as f:
        for line in f:
            if(count == 0):
                count+=1
                continue
            row = re.split(",", line)
            filename = row[1]
            cat = row[0]
            dst_dir = os.path.join(copy_dir, cat)
            if(not os.path.exists(dst_dir)):
                os.mkdir(dst_dir, mode = 0o777)
            try:
                shutil.copy(os.path.join(folder, filename), dst_dir)
            except FileNotFoundError:
                print("Not found: ", os.path.join(folder, filename))
                continue
            count += 1
    print("Transferred images: " + str(count))


folder  =  "C:/Users/shrey/Downloads/dataset/Final/ISIA_Food500/ISIA_Food500/images/"

copy_dir_test = "C:/Users/shrey/Downloads/dataset/Final/ISIA_Food500/ISIA_Food500/FoodCap500/test"
test_file = "C:/Users/shrey/Downloads/dataset/Final/ISIA_Food500/ISIA_Food500/retrieval_dict/metadata_test.csv"
tranfer(test_file, copy_dir_test, folder)

copy_dir_train = "C:/Users/shrey/Downloads/dataset/Final/ISIA_Food500/ISIA_Food500/FoodCap500/train"
train_file = "C:/Users/shrey/Downloads/dataset/Final/ISIA_Food500/ISIA_Food500/retrieval_dict/metadata_train.csv"
tranfer(train_file, copy_dir_train, folder)
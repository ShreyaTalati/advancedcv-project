import unidecode
import os

folder  =  "C:/Users/shrey/Downloads/dataset/Final/ISIA_Food500/ISIA_Food500/images/"
for (dir_path, dir_names, file_names) in os.walk(folder):
    new_dir_path = unidecode.unidecode(dir_path)
    os.rename(dir_path, new_dir_path)
    for file_n in file_names:
        file_path = os.path.join(new_dir_path, file_n)
        new_file_path = unidecode.unidecode(file_path)
        os.rename(file_path, new_file_path)

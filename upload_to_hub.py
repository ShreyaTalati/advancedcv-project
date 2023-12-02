from huggingface_hub import login
from datasets import load_dataset

login(token="xyz")
dataset = load_dataset("imagefolder", data_dir="C:/Users/shrey/Downloads/dataset/Final/ISIA_Food500/ISIA_Food500/", split="train")
dataset.push_to_hub("advancedcv/Food500Cap_train")


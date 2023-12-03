from huggingface_hub import login
from datasets import load_dataset

# Replace the logen token
login(token="xyz")
#train
dataset = load_dataset("imagefolder", data_dir="C:/Users/shrey/Downloads/dataset/Final/ISIA_Food500/ISIA_Food500/FoodCap500/train", split="train")
dataset.push_to_hub("advancedcv/Food500Cap")

#test
dataset = load_dataset("imagefolder", data_dir="C:/Users/shrey/Downloads/dataset/Final/ISIA_Food500/ISIA_Food500/FoodCap500/test", split="test")
dataset.push_to_hub("advancedcv/Food500Cap_test")


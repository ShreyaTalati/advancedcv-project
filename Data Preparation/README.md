We are using [FoodCap500 dataset](https://github.com/aaronma2020/Food500-Cap) for fine-tuning and testing. The FoodCap500 dataset has two `.json` files for finetuning (`finetune_data.json`) and evaluation (`evaluation_data.json`) each. These files mention the filename from the [ISIA-Food500](http://123.57.42.89/FoodComputing-Dataset/ISIA-Food500.html) dataset, category and caption. We follow the below steps to transfer images from the ISIA-Food500 dataset to obtain the FoodCap500 dataset images corresponding to the filenames mentioned in the `.json` files. We also process the data to remove accent from the filenames and captions.

The steps to generate and upload the dataset are:
1. Convert the `.json` files to `.csv` files using the online tool.
2. Run the file `remove_accent_in_images.py` to remove accent from the files and directories present in the dataset.
2. Run the file `remove_accent_in_captions.py` to remove accent from the captions and categories present in the feature file.
3. Run the file `create_FoodCap500_images.py` to transfer images from the ISIA-Food500 dataset to the FoodCap500 dataset folder.
4. Run the file `upload_to_hub.py` by replacing your login token to upload the dataset to the [huggingface repository](https://huggingface.co/advancedcv).
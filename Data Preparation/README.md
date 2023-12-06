We are using [FoodCap500 dataset](https://github.com/aaronma2020/Food500-Cap) for fine-tuning and testing. The FoodCap500 dataset has two `.json` files for finetuning (`finetune_data.json`) and evaluation (`evaluation_data.json`) each. These files mention the filename from the [ISIA-Food500](http://123.57.42.89/FoodComputing-Dataset/ISIA-Food500.html) dataset, category and caption. We follow the below steps to transfer images from the ISIA-Food500 dataset to obtain the FoodCap500 dataset images corresponding to the filenames mentioned in the `.json` files. We also process the data to remove accent from the filenames and captions.

We relied on the dataset stored on Hugging Face for experiments with BLIP-2. The steps to generate and upload the dataset are:
1. Convert the `.json` files to `.csv` files using the online tool.
2. Run the file `remove_accent_in_images.py` to remove accent from the files and directories present in the dataset.
2. Run the file `remove_accent_in_captions.py` to remove accent from the captions and categories present in the feature file.
3. Run the file `create_FoodCap500_images.py` to transfer images from the ISIA-Food500 dataset to the FoodCap500 dataset folder.
4. Run the file `upload_to_hub.py` by replacing your login token to upload the dataset to the [huggingface repository](https://huggingface.co/advancedcv).

For MiniGPT-4 fine-tuning, we followed the instrctuion to prepare our food data in the same format of the dataset the authors used for stage 2 fine-tuning (https://github.com/Vision-CAIR/MiniGPT-4/blob/main/dataset/README_2_STAGE.md). The steps to generate this dataset are:
1. Run the file `minigpt4-dataset-creation.py` to transfer images from the ISIA-Food500 dataset to the FoodCap500 dataset folder.
2. Download `finetune_data.json` and run `Prepare MiniGPT4 caption.ipynb` to get two json files `filter_cap.json` and `filter_cap_challenging.json` in the required format for stage 2 fine-tuning.
3. Run `clean_file_name.ipynb` to convert image names obtained from step 1 to lower cases and check if every image name listed in `filter_cap.json` has a matching image.
4. Put the dataset folder from step 1 and `filter_cap.json` in one folder as the dataset for MiniGPT-4 fine-tuning. For out-of-distribution finetuning, use `filter_cap_challenging.json` and rename it to `filter_cap.json`, which excludes images of our identified challenging labels from fine-tuning data.

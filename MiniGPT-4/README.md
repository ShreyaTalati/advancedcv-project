This folder contains all code and results for experiments with MiniGPT-4 models. We used Vicuna 7B as the backbone LLM. More information available at https://github.com/Vision-CAIR/MiniGPT-4

This folder contains all code and results for experiments with BLIP-2 models.
- `MiniGPT-4 Finetuning.ipynb`: Code for fine-tuning MiniGPT-4 on the entire fine-tuning set of Food-500 Cap and fine-tuning the out-of-distribution (OOD) model on the fine-tuning set excluding images from the 13 identified challenging labels from Chinese, Indian, and Japanese cusines. Detailed instructions are included in the script.
- `MiniGPT-4 Inference.ipynb`: Code for generating captions on the test set with different MiniGPT-4 models. Detailed instructions are included in the script. The original MiniGPT-4 (Vicuna 7B) model can be downloaded from https://github.com/Vision-CAIR/MiniGPT-4. The model fine-tuned on entire fine-tuning set can be downloaded at https://drive.google.com/file/d/1wd8BPy0HOvPE9CG35dKhw03BQS_WdOZW/view?usp=sharing. The OOD fine-tuned model can be downloaded at https://drive.google.com/file/d/1yVaKLUdgsnQqcy2ZhNRBYQtbn2FDgZUe/view?usp=sharing.
- `MiniGPT4_and_GPT4V_Evaluation`: Code for computing captioning performance metrics and selecting example images for different MiniGPT-4 models and GPT-4V results.
- `filter_cap.json`: File containing information for the entire fine-tuning set of Food-500 Cap. See https://github.com/Vision-CAIR/MiniGPT-4/blob/main/dataset/README_2_STAGE.md.
- `filter_cap_challenging.json`: File containing information for the fine-tuning set of Food-500 Cap excluding samples of the 13 challenging labels. Replace `filter_cap.json` by `filter_cap_challenging.json` to fine-tune the OOD model.
- `Results/`
  - `MiniGPT4_finetuned_all_results_30.npy`: Generated captions with 30 maximum tokens on the test set of Food-500 Cap using the fine-tuned MiniGPT-4 model
  - `MiniGPT4_finetuned_all_results_60.npy`: Generated captions with 60 maximum tokens on the test set of Food-500 Cap using the fine-tuned MiniGPT-4 model
  - `MiniGPT4_finetuned_challenging_results_30.npy`: Generated captions with 30 maximum tokens on the test set of Food-500 Cap using the fine-tuned OOD MiniGPT-4 model
  - `MiniGPT4_finetuned_challenging_results_60.npy`: Generated captions with 60 maximum tokens on the test set of Food-500 Cap using the fine-tuned OOD MiniGPT-4 model
  - `MiniGPT4_original_results_30.npy`: Generated captions with 30 maximum tokens on the test set of Food-500 Cap using the original MiniGPT-4 model
  - `MiniGPT4_original_results_60.npy`: Generated captions with 60 maximum tokens on the test set of Food-500 Cap using the original MiniGPT-4 model

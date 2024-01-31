# Format-OCR-Net

Codes for dataset construction and processing, and model training and tuning of Formatted Document OCR.

## Environments

<div align="center">

![](https://img.shields.io/badge/GPU-RTX%204080-green?logo=nvidia) ![](https://img.shields.io/badge/NVIDIA%20Driver-535.154.05-blue?logo=nvidia) ![](https://img.shields.io/badge/CUDA-12.2-blue?logo=nvidia)

![](https://img.shields.io/badge/Ubuntu-22.04.3%20LTS-blue?logo=ubuntu) ![](https://img.shields.io/badge/Python-3.11.7-blue?logo=python) ![](https://img.shields.io/badge/PyTorch-2.1.2-blue?logo=pytorch)
</div>


## Download dataset

<div align="center">

[LaTeX-OCR](https://github.com/lukas-blecher/LaTeX-OCR) ([dataset](https://drive.google.com/drive/folders/13CA4vAmOmD_I_dSbvLp-Lf0s6KiaNfuO)) · [im2latex](https://github.com/luopeixiang/im2latex) ([dataset](https://huggingface.co/datasets/yuntian-deng/im2latex-100k/tree/main/data))
  
</div>


```sh
# pip install huggingface_hub
# For PRC users, hf-mirror is recommended
HF_ENDPOINT=https://hf-mirror.com HF_HUB_ENABLE_HF_TRANSFER=1 huggingface-cli download yuntian-deng/im2latex-100k --include "*.parquet" --repo-type dataset --local-dir ./datasets
```
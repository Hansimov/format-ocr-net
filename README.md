# Format-OCR-Net

Codes for dataset construction and processing, and model training and tuning of Formatted Document OCR.

## Environments

<div align="center">

![](https://img.shields.io/badge/GPU-RTX%204080-green?logo=nvidia) ![](https://img.shields.io/badge/NVIDIA%20Driver-535.154.05-blue?logo=nvidia) ![](https://img.shields.io/badge/CUDA-12.2-blue?logo=nvidia)

![](https://img.shields.io/badge/Ubuntu-22.04.3%20LTS-blue?logo=ubuntu) ![](https://img.shields.io/badge/Python-3.11.7-blue?logo=python) ![](https://img.shields.io/badge/PyTorch-2.1.2-blue?logo=pytorch)
</div>


### Ubuntu dependencies

```sh
sudo apt install imagemagick texlive-latex-extra sympy dvipng
```

### Python requirements

```sh
pip install -r requirements.txt
```

## Download dataset

<div align="center">

[LaTeX-OCR](https://github.com/lukas-blecher/LaTeX-OCR) ([dataset](https://drive.google.com/drive/folders/13CA4vAmOmD_I_dSbvLp-Lf0s6KiaNfuO)) · [im2latex](https://github.com/luopeixiang/im2latex) ([dataset](https://huggingface.co/datasets/yuntian-deng/im2latex-100k/tree/main/data))
  
</div>


```sh
# For PRC users, hf-mirror is recommended
HF_ENDPOINT=https://hf-mirror.com HF_HUB_ENABLE_HF_TRANSFER=1 huggingface-cli download yuntian-deng/im2latex-100k --include "*.parquet" --repo-type dataset --local-dir ./datasets
```

If above command failed, please download the dataset mannually.


## Architecture and models

### Notes from EasyOCR

See: [Implementation Roadmap  of EasyOCR](https://github.com/JaidedAI/EasyOCR/blob/master/README.md#implementation-roadmap)

> **Detection** execution uses the **CRAFT** algorithm from this [official repository](https://github.com/clovaai/CRAFT-pytorch) and their [paper](https://arxiv.org/abs/1904.01941) (Thanks @YoungminBaek from [@clovaai](https://github.com/clovaai)). We also use their pretrained model. Training script is provided by [@gmuffiness](https://github.com/gmuffiness).
> 
> **Recognition** model is a **CRNN** ([paper](https://arxiv.org/abs/1507.05717)). It is composed of 3 main components: feature extraction (we are currently using [**Resnet**](https://arxiv.org/abs/1512.03385)) and **VGG**, sequence labeling ([**LSTM**](https://www.bioinf.jku.at/publications/older/2604.pdf)) and decoding ([**CTC**](https://www.cs.toronto.edu/~graves/icml_2006.pdf)). The training pipeline for recognition execution is a modified version of the [deep-text-recognition-benchmark](https://github.com/clovaai/deep-text-recognition-benchmark) framework. (Thanks [@ku21fan](https://github.com/ku21fan) from [@clovaai](https://github.com/clovaai)) This repository is a gem that deserves more recognition.
> 
> **Beam search** code is based on this [repository](https://github.com/githubharald/CTCDecoder) and his [blog](https://towardsdatascience.com/beam-search-decoding-in-ctc-trained-neural-networks-5a889a3d85a7). (Thanks [@githubharald](https://github.com/githubharald))
> 
> **Data synthesis** is based on [TextRecognitionDataGenerator](https://github.com/Belval/TextRecognitionDataGenerator). (Thanks [@Belval](https://github.com/Belval))


See also: [deep-text-recognition-benchmark](https://github.com/clovaai/deep-text-recognition-benchmark?tab=readme-ov-file#what-is-wrong-with-scene-text-recognition-model-comparisons-dataset-and-model-analysis) of [Page 6](https://arxiv.org/pdf/1904.01906.pdf)

![](https://github.com/clovaai/deep-text-recognition-benchmark/raw/master/figures/trade-off.png)

### Nots from PaddleOCR

See:
- [FAQ - PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.7/doc/doc_ch/FAQ.md)
- [前沿算法与模型 - PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.7/doc/doc_ch/algorithm_overview.md)
- [Recognition - PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.7/doc/doc_ch/recognition.md)
- [模型库概览 - PaddleClas](https://github.com/PaddlePaddle/PaddleClas/tree/release/2.5/docs/zh_CN/models/ImageNet1k)


> ### 1.1 检测
> 
> #### Q: 基于深度学习的文字检测方法有哪几种？各有什么优缺点？
> 
> **A**：常用的基于深度学习的文字检测方法一般可以分为基于回归的、基于分割的两大类，当然还有一些将两者进行结合的方法。
> 
> 1. 基于回归的方法分为box回归和像素值回归。 a. 采用box回归的方法主要有CTPN、Textbox系列和EAST，这类算法对规则形状文本检测效果较好，但无法准确检测不规则形状文本。b. 像素值回归的方法主要有CRAFT和SA-Text，这类算法能够检测弯曲文本且对小文本效果优秀但是实时性能不够。
> 2. 基于分割的算法，如PSENet，这类算法不受文本形状的限制，对各种形状的文本都能取得较好的效果，但是往往后处理比较复杂，导致耗时严重。目前也有一些算法专门针对这个问题进行改进，如DB，将二值化进行近似，使其可导，融入训练，从而获取更准确的边界，大大降低了后处理的耗时。
> 
> ### 1.2 识别
> 
> #### Q: PaddleOCR提供的文本识别算法包括哪些？
> 
> A: PaddleOCR主要提供五种文本识别算法，包括CRNN/StarNet/RARE/Rosetta和SRN，其中CRNN/StarNet和Rosetta是基于ctc的文字识别算法，RARE是基于attention的文字识别算法；SRN为百度自研的文本识别算法，引入了语义信息，显著提升了准确率。详情可参照PaddleOCR中“文本识别算法”的对应章节。
> 
> #### Q: 文本识别方法CRNN关键技术有哪些？
> 
> A: CRNN关键技术包括三部分。（1）**CNN**提取图像卷积特征。（2）深层双向**LSTM**网络，在卷积特征的基础上继续提取文字序列特征。（3）Connectionist Temporal Classification (**CTC**)，解决训练时字符无法对齐的问题。
> 
> #### Q: 对于中文行文本识别，CTC和Attention哪种更优？
> 
> **A**：（1）从效果上来看，**通用OCR场景CTC的识别效果优于Attention**，因为带识别的字典中的字符比较多，常用中文汉字三千字以上，如果训练样本不足的情况下，对于这些字符的序列关系挖掘比较困难。中文场景下Attention模型的优势无法体现。而且Attention适合短语句识别，对长句子识别比较差。
> 
> （2）从训练和预测速度上，Attention的串行解码结构限制了预测速度，而**CTC网络结构更高效，预测速度上更有优势**。
> 
> ### 1.3 端到端
> 
> #### Q: 请问端到端的pgnet相比于DB+CRNN在准确率上有优势吗？或者是pgnet最擅长的场景是什么场景呢？
> 
> A: pgnet是端到端算法，检测识别一步到位，不用分开训练2个模型，也支持弯曲文本的识别，但是在中文上的效果还没有充分验证；**db+crnn的验证更充分，应用相对成熟**，常规非弯曲的文本都能解的不错。
> 
> #### Q: 目前OCR普遍是二阶段，端到端的方案在业界落地情况如何？
> 
> **A**：...
> 
> ### 2.3 数据量说明
> 
> #### Q：简单的对于精度要求不高的OCR任务，数据集需要准备多少张呢？
> 
> **A**：...
> 
> #### Q：请问PaddleOCR项目中的中文超轻量和通用模型用了哪些数据集？训练多少样本，gpu什么配置，跑了多少个epoch，大概跑了多久？
> 
> **A**：...
> 
> ### 2.5 预训练模型与微调
> 
> #### Q：如何更换文本检测/识别的backbone？
> 
> A：无论是文字检测，还是文字识别，骨干网络的选择是预测效果和预测效率的权衡。一般，选择更大规模的骨干网络，例如**ResNet**101_vd，则检测或识别更准确，但预测耗时相应也会增加。而选择更小规模的骨干网络，例如**MobileNet**V3_small_x0_35，则预测更快，但检测或识别的准确率会大打折扣。
> 
> 幸运的是不同骨干网络的检测或识别效果与在ImageNet数据集图像1000分类任务效果正相关。飞桨图像分类套件PaddleClas汇总了ResNet_vd、Res2Net、HRNet、MobileNetV3、GhostNet等23种系列的分类网络结构，在上述图像分类任务的top1识别准确率，GPU(V100和T4)和CPU(骁龙855)的预测耗时以及相应的117个预训练模型下载地址。
> 
> ...
>
> ### 2.7 模型结构
> 
> #### Q：文本识别训练不加LSTM是否可以收敛？
> 
> **A**：理论上是可以收敛的，加上LSTM模块主要是为了挖掘文字之间的序列关系，提升识别效果。对于有明显上下文语义的场景效果会比较明显。
> 
> #### Q：文本识别中LSTM和GRU如何选择？
> 
> **A**：从项目实践经验来看，**序列模块采用LSTM的识别效果优于GRU**，但是LSTM的计算量比GRU大一些，可以根据自己实际情况选择。
> 
> #### Q：对于CRNN模型，backbone采用DenseNet和ResNet_vd，哪种网络结构更好？
> 
> **A**：Backbone的识别效果在CRNN模型上的效果，与Imagenet 1000 图像分类任务上识别效果和效率一致。在图像分类任务上**ResnNet_vd（79%+）的识别精度明显优于DenseNet（77%+）**，此外对于GPU，Nvidia针对ResNet系列模型做了优化，预测效率更高，所以相对而言，**resnet_vd是较好选择。如果是移动端，可以优先考虑MobileNetV3系列。**
> 
> #### Q:  如何根据不同的硬件平台选用不同的backbone？
> 
> **A**：在不同的硬件上，不同的backbone的速度优势不同，可以根据不同平台的速度-精度图来确定backbone，这里可以参考[**PaddleClas模型速度-精度图**](https://github.com/PaddlePaddle/PaddleClas/tree/release/2.5/docs/zh_CN/models/ImageNet1k#Overview)。
> 


See also:

#### Performance of the server models

![](https://github.com/PaddlePaddle/PaddleClas/raw/release/2.5/docs/images/models/V100_benchmark/v100.fp32.bs1.main_fps_top1_s.png)

#### Performance of the VisionTransformer models

![](https://github.com/PaddlePaddle/PaddleClas/blob/release/2.5/docs/images/models/V100_benchmark/v100.fp32.bs1.visiontransformer.png)

## References

- Custom recognition models - EasyOCR
    - https://github.com/JaidedAI/EasyOCR/blob/master/custom_model.md
- deep-text-recognition-benchmark - GitHub
    - https://github.com/clovaai/deep-text-recognition-benchmark
- OCR benchmark on PaperswithCode
    - https://paperswithcode.com/task/optical-character-recognition
- untrix/im2latex - GitHub
    - https://github.com/untrix/im2latex
    - https://untrix.github.io/i2l/
- PP-OCR系列模型列表（V4，2023年8月1日更新）
    - https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.7/doc/doc_ch/models_list.md
- FAQ of PaddleOCR
    - https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.7/doc/doc_ch/FAQ.md
- References of EasyOCR
    - https://github.com/JaidedAI/EasyOCR?tab=readme-ov-file#acknowledgement-and-references
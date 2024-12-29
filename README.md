# HRRPGraphNet
We got accepted to IET Electronics Letters!
HRRPGraphNet is a deep learning model for processing HRRP data using graph neural networks💥.

## Usage

To train and test the model, run `main.py`.

## Dependencies
- Python 3.8
- PyTorch 2.2.0

## Dataset

The dataset should be organized in the `data/` directory with the following structure:

```
data/
├── train/
└── test/
```

## Model

The model is defined in `models.py` and consists of convolutional layers followed by graph convolutional layers.

## License

This project is licensed under the MIT License.

## Citation
please kindly cite this paper if our HRRPGraphNet can give you any inspiration for your research, thanks a lot.

```
@article{https://doi.org/10.1049/ell2.70088,
author = {Chen, Lingfeng and Sun, Xiao and Pan, Zhiliang and Liu, Qi and Wang, Zehao and Su, Xiaolong and Liu, Zhen and Hu, Panhe},
title = {HRRPGraphNet: Make HRRPs to be graphs for efficient target recognition},
journal = {Electronics Letters},
volume = {60},
number = {22},
pages = {e70088},
keywords = {graphs, radar signal processing, radar target recognition},
doi = {https://doi.org/10.1049/ell2.70088},
url = {https://ietresearch.onlinelibrary.wiley.com/doi/abs/10.1049/ell2.70088},
year = {2024}
}
```

## Contact

Lingfeng Chen

Email: chenlingfeng@nudt.edu.cn

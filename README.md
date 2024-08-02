# HRRPGraphNet

HRRPGraphNet is a deep learning model for processing HRRP data using graph neural networks.

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
@inproceedings{Chen2024HRRPGraphNetAG,
  title={HRRPGraphNet: A Graph Neural Network Based Approach for HRRP Radar Target Recognition},
  author={Lingfeng Chen and Panhe Hu and Zhiliang Pan and Xiao Sun and Zehao Wang},
  year={2024},
  url={https://api.semanticscholar.org/CorpusID:271097314}
}
```

## Contact

Lingfeng Chen

Email: chenlingfeng@nudt.edu.cn

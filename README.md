# HRRP GraphNet

HRRP GraphNet is a deep learning model for processing HRRP data using graph neural networks.

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

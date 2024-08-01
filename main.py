import torch
from dataset import HRRPDataset
from models import HRRPGraphNet
from train import trainAndTest_model
from utils import generate_distance_matrix
import numpy as np

# Set random seed for reproducibility
seed_n = 56
torch.manual_seed(seed_n)
np.random.seed(seed_n)

# Set device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Create dataset instances
dataset = HRRPDataset(root_dir='train')
test_dataset = HRRPDataset(root_dir='test')

# Generate distance matrix
N = 500  # Example feature size
distance_matrix = generate_distance_matrix(N).to(device)

# Create model instance
num_classes = len(dataset.labels)
model = HRRPGraphNet(num_classes=num_classes)
model.to(device)

# Train and test the model
trainAndTest_model(model, dataset, test_dataset, distance_matrix, learning_rate=0.0005, num_epochs=300, device=device)
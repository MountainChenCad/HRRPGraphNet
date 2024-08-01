import os
import torch
from torch.utils.data import Dataset
from scipy.io import loadmat


class HRRPDataset(Dataset):
    def __init__(self, root_dir, transform=None):
        self.root_dir = root_dir
        self.file_list = [f for f in os.listdir(root_dir) if f.endswith('.mat')]
        self.transform = transform
        self.labels = {target: i for i, target in enumerate(["F15", "IDF", "F18"])}

    def __len__(self):
        return len(self.file_list)

    def __getitem__(self, idx):
        file_path = os.path.join(self.root_dir, self.file_list[idx])
        data = torch.from_numpy(loadmat(file_path)['CoHH']).float()
        label = self.labels[self.extract_target_name(self.file_list[idx])]
        label = torch.tensor(label, dtype=torch.long)
        return data, label

    def extract_target_name(self, file_name):
        return file_name.split('_')[0]

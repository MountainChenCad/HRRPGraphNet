import torch

def generate_distance_matrix(N):
    distance_matrix = torch.zeros(N, N, dtype=torch.float32)
    for i in range(N):
        for j in range(N):
            distance_matrix[i, j] = 1 / (abs(i - j) + 1)
    return distance_matrix
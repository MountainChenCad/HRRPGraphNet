import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.nn.init import xavier_uniform_, zeros_

class GraphConvLayer(nn.Module):
    def __init__(self, in_channels, out_channels):
        super(GraphConvLayer, self).__init__()
        self.weight1 = nn.Parameter(torch.FloatTensor(in_channels, out_channels))
        self.weight2 = nn.Parameter(torch.FloatTensor(in_channels, out_channels))
        self.bias = nn.Parameter(torch.FloatTensor(out_channels))
        xavier_uniform_(self.weight1)
        xavier_uniform_(self.weight2)
        zeros_(self.bias)

    def forward(self, x, adj):
        x = x.transpose(1, 2)
        adj = adj.squeeze(1)
        support = torch.matmul(adj, x)
        out = torch.matmul(support, self.weight1) + torch.matmul(x, self.weight2) + self.bias
        out = out.transpose(1, 2)
        return out

class HRRPGraphNet(nn.Module):
    def __init__(self, num_classes):
        super(HRRPGraphNet, self).__init__()
        self.conv1 = nn.Conv1d(1, 16, kernel_size=3, padding=1)
        self.bn1 = nn.BatchNorm1d(16)
        self.graph_conv = GraphConvLayer(16, 32)
        self.leakyrelu = nn.LeakyReLU(0.1)
        self.attention = nn.Linear(500, 1)
        xavier_uniform_(self.attention.weight)
        zeros_(self.attention.bias)
        self.fc = nn.Linear(500, num_classes)  # Adjust input features if necessary
        xavier_uniform_(self.fc.weight)
        zeros_(self.fc.bias)

    def construct_adj_matrix(self, x, distance_matrix):
        batch_size, _, N = x.size()
        x_transposed = x.transpose(1, 2)
        adj_matrix = torch.bmm(x_transposed, x)
        distance_matrix = distance_matrix.unsqueeze(0).expand(batch_size, -1, -1)
        adj_matrix = adj_matrix * distance_matrix
        adj_tensor = adj_matrix.unsqueeze(1)
        return adj_tensor

    def forward(self, x, distance_matrix):
        adj = self.construct_adj_matrix(x, distance_matrix)
        x = self.leakyrelu(self.bn1(self.conv1(x)))
        x = self.graph_conv(x, adj)
        attention_weights = F.softmax(self.attention(x), dim=1)
        x = torch.sum(x * attention_weights, dim=1)
        x = self.fc(x)
        return x
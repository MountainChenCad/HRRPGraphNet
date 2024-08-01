import torch
from dataset import HRRPDataset
from models import HRRPGraphNet
import torch.nn as nn
import numpy as np
from torch.utils.data import DataLoader

def trainAndTest_model(model, dataset, test_dataset, distance_matrix, learning_rate, num_epochs, device):
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
    criterion = nn.CrossEntropyLoss()

    model.train()
    data_loader = DataLoader(dataset, batch_size=128, shuffle=False)
    loss_values = []
    best_loss = float('inf')
    history_acc = []
    for epoch in range(num_epochs):
        for batch_idx, (data, labels) in enumerate(data_loader):
            data, labels = data.to(device), labels.long().to(device)
            optimizer.zero_grad()
            outputs = model(data, distance_matrix)
            l2_loss = sum(p.norm(2) for p in model.parameters())
            loss = criterion(outputs, labels) + 0.01 * l2_loss
            loss.backward()
            optimizer.step()

            loss_values.append(loss.item())
            current_loss = loss.item()

            if current_loss < best_loss:
                best_loss = current_loss

                print(
                    f'New best batch loss model saved at Epoch {epoch + 1}, Batch {batch_idx + 1} with loss: {best_loss:.4f}')

        print(f'Epoch [{epoch + 1}/{num_epochs}] completed.')

        model.eval()
        test_loader = DataLoader(test_dataset, batch_size=128, shuffle=False)
        all_labels = []
        predicted_labels = []
        with torch.no_grad():
            for data, labels in test_loader:
                data, labels = data.to(device), labels.long().to(device)
                outputs = model(data, distance_matrix)
                _, predicted = torch.max(outputs.data, 1)
                predicted_labels.extend(predicted.cpu().numpy())
                all_labels.extend(labels.cpu().numpy())


        accuracy = 100 * np.sum(np.array(predicted_labels) == np.array(all_labels)) / len(all_labels)
        print(f'Accuracy on test set: {accuracy:.2f}%')
        history_acc.append(accuracy)

        label_to_count = {i: 0 for i in range(len(dataset.labels))}
        correct_predictions_per_label = {i: 0 for i in range(len(dataset.labels))}

        for true_label, pred_label in zip(all_labels, predicted_labels):
            label_to_count[true_label] += 1
            if true_label == pred_label:
                correct_predictions_per_label[true_label] += 1

        class_accuracies = {label: (correct / count) * 100 for label, correct, count in zip(
            correct_predictions_per_label.keys(), correct_predictions_per_label.values(), label_to_count.values()) if
                            count > 0}

        for label, accuracy in class_accuracies.items():
            print(f"Class {label}: Accuracy = {accuracy:.2f}%")

    best_average_accuracy = max(history_acc)
    print(f'Best average accuracy over all epochs: {best_average_accuracy:.2f}%')

import numpy as np
import PIL
import random
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix
from datasets import load_dataset, Dataset
import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision.transforms.functional import pil_to_tensor, to_tensor
from torchvision import transforms, models
from torch.utils.data import DataLoader
from torch import optim

transformation_train = transforms.Compose([
    transforms.Resize(size=(240, 180), antialias=True),
    transforms.RandomHorizontalFlip(p=0.5),
    transforms.RandomRotation(15),
    transforms.ToTensor()
])
transformation_test = transforms.Compose([
        transforms.Resize(size=(240, 180), antialias=True),
        transforms.ToTensor()
])

# Transformation applied to train data
def transform_fly(samples):
    samples["pixel_values"] = [transformation_train(image) for image in samples["image"]]
    del samples["image"]
    return samples
    
# Transformation applied to test data
def transform_test_data(samples):
    samples["pixel_values"] = [transformation_test(image) for image in samples["image"]]
    del samples["image"]
    return samples

#Collate function
def collate_fn(examples):
    images = []
    labels = []
    for example in examples:
        images.append(example["pixel_values"])
        labels.append(example["label"])

    pixel_values = torch.stack(images)
    labels = torch.tensor(labels)

    return pixel_values, labels


def train(model, tensor_data, optimizer, criteria, epoch, device='cpu'):

    loss_values = []
    for image, label in tensor_data:
        image = image.to(device)
        label = label.to(device)
        predict = model(image)
        loss = criteria(predict, label)
        loss_value = loss.detach().cpu()
        loss_values.append(loss_value.item())
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
    num_correct = 0
    total = 0
    model.eval()
    with torch.no_grad():
        for image, label in tensor_data:
            image = image.to(device)
            label = label.to(device)    
            predict = model(image)
            _, score = predict.max(1)
            num_correct += (score == label).sum()
            total += score.size(0) 
        model.train()
    train_accuracy = num_correct * 100 / total

    return optimizer, train_accuracy, loss_values      

def test(model, tensor_data, device='cpu'):
    
    num_correct = 0
    total = 0
    model.eval()
    probabilities, test_labels = [], []        
    with torch.no_grad():
        for image, label in tensor_data:
            test_labels.append(label)
            image = image.to(device=device)
            label = label.to(device=device)
            preds = model(image)
            prob = F.softmax(preds, dim=1)
            prob = prob.cpu()
            probabilities.append(prob.numpy())
            _, score = preds.max(1)
            num_correct += (score == label).sum()
            total += score.size(0)

    model.train()       
    accuracy = num_correct * 100 / total

    return accuracy, probabilities, test_labels

    
class ModelCars(nn.Module):

    def __init__(self, model, transformation, device='cpu'):
        super(ModelCars, self).__init__()
        self.model = model
        self.transform = transformation
        self.device = device

    def forward(self, x):
        x = self.transform(x)
        x_shape = x.shape
        x = torch.reshape(x, (1,*x_shape)).to(self.device)
        x = self.model(x)
        return F.softmax(x)    
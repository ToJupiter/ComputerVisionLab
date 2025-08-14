"""
    Data: https://www.kaggle.com/datasets/khazi1/city-scape

"""

import kagglehub
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import numpy as np
import cv2
import os
import json
from PIL import Image
import matplotlib.pyplot as plt
from tqdm import tqdm
import albumentations as A
from albumentations.pytorch import ToTensorV2
import math

# Cell 2: Dataset class for Cityscapes
class CityscapesDataset(Dataset):
    def __init__(self, image_dir, label_dir, transform=None, split='train'):
        self.image_dir = image_dir
        self.label_dir = label_dir
        self.transform = transform
        self.split = split
        
        # Get image paths
        self.image_paths = []
        self.label_paths = []
        
        split_dir = os.path.join(image_dir, split)
        label_split_dir = os.path.join(label_dir, split)
        
        for city in os.listdir(split_dir):
            city_img_dir = os.path.join(split_dir, city)
            city_label_dir = os.path.join(label_split_dir, city)
            
            if os.path.isdir(city_img_dir):
                for img_file in os.listdir(city_img_dir):
                    if img_file.endswith('_leftImg8bit.png'):
                        img_path = os.path.join(city_img_dir, img_file)
                        label_file = img_file.replace('_leftImg8bit.png', '_gtFine_labelIds.png')
                        label_path = os.path.join(city_label_dir, label_file)
                        
                        if os.path.exists(label_path):
                            self.image_paths.append(img_path)
                            self.label_paths.append(label_path)
    
    def __len__(self):
        return len(self.image_paths)
    
    def __getitem__(self, idx):
        image = cv2.imread(self.image_paths[idx])
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        label = cv2.imread(self.label_paths[idx], cv2.IMREAD_GRAYSCALE)
        
        # Convert Cityscapes labels to 19 classes
        label = self.convert_labels(label)
        
        if self.transform:
            transformed = self.transform(image=image, mask=label)
            image = transformed['image']
            label = transformed['mask']
        
        return image, label.long()
    
    def convert_labels(self, label):
        # Cityscapes label mapping to 19 classes
        label_mapping = {
            7: 0, 8: 1, 11: 2, 12: 3, 13: 4, 17: 5, 19: 6, 20: 7, 21: 8, 22: 9,
            23: 10, 24: 11, 25: 12, 26: 13, 27: 14, 28: 15, 31: 16, 32: 17, 33: 18
        }
        
        new_label = np.full(label.shape, 255, dtype=np.uint8)
        for old_id, new_id in label_mapping.items():
            new_label[label == old_id] = new_id
        
        return new_label

# Cell 9: Data transforms and loaders
def get_transforms():
    train_transform = A.Compose([
        A.Resize(512, 1024),
        A.HorizontalFlip(p=0.5),
        A.RandomBrightnessContrast(p=0.2),
        A.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ToTensorV2()
    ])
    
    val_transform = A.Compose([
        A.Resize(512, 1024),
        A.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ToTensorV2()
    ])
    
    return train_transform, val_transform

# Setup dataset paths
image_dir = '/kaggle/input/city-scape/leftImg8bit_trainvaltest/leftImg8bit'
label_dir = '/kaggle/input/city-scape/gtFine_trainvaltest/gtFine'

train_transform, val_transform = get_transforms()

train_dataset = CityscapesDataset(image_dir, label_dir, transform=train_transform, split='train')
val_dataset = CityscapesDataset(image_dir, label_dir, transform=val_transform, split='val')

train_loader = DataLoader(train_dataset, batch_size=2, shuffle=True, num_workers=2)
val_loader = DataLoader(val_dataset, batch_size=2, shuffle=False, num_workers=2)

print(f"Train dataset size: {len(train_dataset)}")
print(f"Validation dataset size: {len(val_dataset)}")
#!/usr/bin/env python3
import os
import random
import shutil

# Define the paths to your "yes" and "no" folders
yes_folder = "yes"
no_folder = "no"

# Create directories for the train, validation, and test sets
os.makedirs("train/yes", exist_ok=True)
os.makedirs("train/no", exist_ok=True)
os.makedirs("validation/yes", exist_ok=True)
os.makedirs("validation/no", exist_ok=True)
os.makedirs("test/yes", exist_ok=True)
os.makedirs("test/no", exist_ok=True)

# List the files in the "yes" and "no" folders
yes_files = os.listdir(yes_folder)
no_files = os.listdir(no_folder)

# Set the random seed for reproducibility
random.seed(42)

# Shuffle the file lists
random.shuffle(yes_files)
random.shuffle(no_files)

# Define the proportions for train, validation, and test sets
train_ratio = 0.7
val_ratio = 0.1
test_ratio = 0.2

# Split the data into train, validation, and test sets
train_yes = yes_files[:int(len(yes_files) * train_ratio)]
val_yes = yes_files[int(len(yes_files) * train_ratio):int(len(yes_files) * (train_ratio + val_ratio))]
test_yes = yes_files[int(len(yes_files) * (train_ratio + val_ratio)):]

train_no = no_files[:int(len(no_files) * train_ratio)]
val_no = no_files[int(len(no_files) * train_ratio):int(len(no_files) * (train_ratio + val_ratio))]
test_no = no_files[int(len(no_files) * (train_ratio + val_ratio)):]

# Move the files to the respective directories
for file in train_yes:
    shutil.copy(os.path.join(yes_folder, file), os.path.join("train/yes", file))

for file in val_yes:
    shutil.copy(os.path.join(yes_folder, file), os.path.join("validation/yes", file))

for file in test_yes:
    shutil.copy(os.path.join(yes_folder, file), os.path.join("test/yes", file))

for file in train_no:
    shutil.copy(os.path.join(no_folder, file), os.path.join("train/no", file))

for file in val_no:
    shutil.copy(os.path.join(no_folder, file), os.path.join("validation/no", file))

for file in test_no:
    shutil.copy(os.path.join(no_folder, file), os.path.join("test/no", file))


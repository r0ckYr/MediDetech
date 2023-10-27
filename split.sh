#!/bin/bash

# Set the source directory
source_dir=$1  # Replace with the path to your "yes" and "no" folders

# Set the destination directory for the dataset
destination_dir=$2

# Create the destination directories if they don't exist
mkdir -p "$destination_dir/train/no"
mkdir -p "$destination_dir/train/yes"
mkdir -p "$destination_dir/test/no"
mkdir -p "$destination_dir/test/yes"
mkdir -p "$destination_dir/validation/no"
mkdir -p "$destination_dir/validation/yes"

# Calculate the number of images for each split (80% train, 10% test, 10% validation)
total_images=$(find "$source_dir" -type f | wc -l)
train_count=$((total_images * 8 / 10))
test_count=$((total_images * 1 / 10))
validation_count=$((total_images * 1 /10))

# Use the 'shuf' command to shuffle the image files randomly and copy them to the destination folders
shuf -zn "$train_count" -e "$source_dir/yes/"* | xargs -0 cp -t "$destination_dir/train/yes"
shuf -zn "$train_count" -e "$source_dir/no/"* | xargs -0 cp -t "$destination_dir/train/no"
shuf -zn "$test_count" -e "$source_dir/yes/"* | xargs -0 cp -t "$destination_dir/test/yes"
shuf -zn "$test_count" -e "$source_dir/no/"* | xargs -0 cp -t "$destination_dir/test/no"
shuf -zn "$validation_count" -e "$source_dir/yes/"* | xargs -0 cp -t "$destination_dir/validation/yes"
shuf -zn "$validation_count" -e "$source_dir/no/"* | xargs -0 cp -t "$destination_dir/validation/no"

echo "Images have been split into train, test, and validation sets with the specified directory structure and copied."


import os
import shutil

og_root = r"C:\Users\Andrew Jeon\OneDrive\Desktop\friendfoe"
new_root = r"C:\Users\Andrew Jeon\OneDrive\Desktop\friendfoe"

# Define the directories to be moved
directories_to_move = ["Images", "labels"]

# Iterate over the directories
for directory in directories_to_move:
    # Create the new parent directory if it doesn't exist
    new_parent_dir = os.path.join(new_root, directory)
    os.makedirs(new_parent_dir, exist_ok=True)

    # Move the train and test directories
    for split in ["train", "test", "valid"]:
        # Define the original and new paths for the split
        original_split_path = os.path.join(og_root, split, directory)
        new_split_path = os.path.join(new_parent_dir, split)

        # Move the directory
        shutil.move(original_split_path, new_split_path)




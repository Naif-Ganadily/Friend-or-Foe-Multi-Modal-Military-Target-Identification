from ultralytics import YOLO
import torch
import os
import shutil



# Directory shifting to match YOLOv8 expected structure

# og_root = r"C:\Users\Andrew Jeon\OneDrive\Desktop\friendfoe"
# new_root = r"C:\Users\Andrew Jeon\OneDrive\Desktop\friendfoe"
#
# # Define the directories to be moved
# directories_to_move = ["Images", "labels"]
#
# # Iterate over the directories
# for directory in directories_to_move:
#     # Create the new parent directory if it doesn't exist
#     new_parent_dir = os.path.join(new_root, directory)
#     os.makedirs(new_parent_dir, exist_ok=True)
#
#     # Move the train and test directories
#     for split in ["train", "test", "valid"]:
#         # Define the original and new paths for the split
#         original_split_path = os.path.join(og_root, split, directory)
#         new_split_path = os.path.join(new_parent_dir, split)
#
#         # Move the directory
#         shutil.move(original_split_path, new_split_path)






if torch.cuda.is_available():
    print("GPU is available!")
else:
    print("GPU is not available. Running on CPU.")



if __name__ == '__main__':
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


    # Load a model
    model = YOLO("yolov8n.yaml")  # build a new model from scratch

    # Use the model
    model.train(data="config.yaml", epochs=30)  # train the model



# yolov8n-seg.yaml






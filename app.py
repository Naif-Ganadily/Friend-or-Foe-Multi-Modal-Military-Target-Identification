# Experimenting with Streamlit 
# Template TODO until we decide on the model and the data

import glob
import streamlit as st
import wget
from PIL import Image
import torch
import cv2
import os
import time



st.set_page_config(layout="wide")

# The model path
cfg_model_path = 'path/.pt'  
model = None

# Function to load the model
@st.cache(allow_output_mutation=True)
def load_model(path):
    model = torch.hub.load('ultralytics/yolov8', 'custom', path=path, force_reload=True)
    return model

# Function to display the image and model predictions
def display_image_and_predictions(img_path, model):
    col1, col2 = st.columns(2)
    with col1:
        st.image(img_path, caption="Uploaded Image")
    with col2:
        img = infer_image(img_path, model)
        st.image(img, caption="Model Prediction")

# Placeholder for model inference (to be replaced with actual model inference code)
def infer_image(img_path, model):
    return Image.open(img_path) 

def main():
    global model

    st.title("Object Recognition Dashboard")

    # Model loading
    if not os.path.isfile(cfg_model_path):
        st.warning("Model file not available!!! Please check the path.", icon="⚠️")
    else:
        model = load_model(cfg_model_path)

    # Image uploading
    img_file_buffer = st.file_uploader("Upload an image", type=['png', 'jpeg', 'jpg'])
    if img_file_buffer is not None:
        img_path = "temp_uploaded_image." + img_file_buffer.name.split('.')[-1]
        with open(img_path, 'wb') as f:
            f.write(img_file_buffer.getbuffer())
        display_image_and_predictions(img_path, model)

if __name__ == "__main__":
    main()
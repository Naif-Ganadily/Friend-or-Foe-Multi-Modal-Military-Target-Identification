# Experimenting with Streamlit 
# Template TODO until we decide on the model and the data

import streamlit as st
from PIL import Image
import cv2
import os
import torch



# Set the page layout and title
st.set_page_config(layout="wide", page_title="🔍 Friend or Foe Detection 🎖️")

# The model path
cfg_model_path = 'models/naif_models/yolov8x_2classes_25epochs/best.pt'  
model = None

# Function to load the model with a message
@st.cache(allow_output_mutation=True)
def load_model(path):
    try:
        with st.spinner('Loading model... 🚀'):
            model = torch.hub.load('ultralytics/yolov8', 'custom', path=path, force_reload=True)
        return model
    except Exception as e:
        st.error(f"Failed to load model: {e}")
        return None

# Function to display the image and model predictions
def display_image_and_predictions(img_path, model):
    col1, col2 = st.columns(2)
    with col1:
        st.image(img_path, caption="Uploaded Image 📷")
    with col2:
        st.write("Analyzing... ⚔️ Please wait!")
        img = infer_image(img_path, model)
        st.image(img, caption="Detection Results 🛡️")

# Updated model inference function
def infer_image(img_path, model):
    img = cv2.imread(img_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = model(img_rgb)
    results.render() 
    img_pil = Image.fromarray(cv2.cvtColor(results.imgs[0], cv2.COLOR_BGR2RGB))
    return img_pil

def main():
    global model

    st.title("🔍 Friend or Foe Detection Dashboard 🎖️")

    if not os.path.isfile(cfg_model_path):
        st.warning("Model file not available! Please check the path. 🚫")
    else:
        model = load_model(cfg_model_path)

    img_file_buffer = st.file_uploader("Upload an image 🖼️ (png, jpeg, jpg)", type=['png', 'jpeg', 'jpg'])
    if img_file_buffer is not None:
        img_path = "temp_uploaded_image." + img_file_buffer.name.split('.')[-1]
        with open(img_path, 'wb') as f:
            f.write(img_file_buffer.getbuffer())
        display_image_and_predictions(img_path, model)

if __name__ == "__main__":
    main()
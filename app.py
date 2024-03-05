import glob
import streamlit as st
from PIL import Image
import torch
import cv2
import os
import time
from ultralytics import YOLO


# Set the page configuration
st.set_page_config(layout="wide", page_title="Friend or Foe 🌟", page_icon="🌟")

model = None
confidence = 0.25

def save_uploaded_file(directory, img_bytes):
    if not os.path.exists(directory):
        os.makedirs(directory)
    img_file_path = os.path.join(directory, "upload." + img_bytes.name.split('.')[-1])
    with open(img_file_path, "wb") as f:
        f.write(img_bytes.getbuffer())
    return img_file_path

def image_input(img_file):
    if img_file:
        col1, col2 = st.columns(2)
        with col1:
            st.image(img_file, caption="Your Selected Image 📸")
        with col2:
            if model is not None:
                st.markdown("### Model Predictions 🎯")
                infer_image(img_file)
            else:
                st.error("Model not loaded. Please upload a model.")

def infer_image(img_path):
    img = cv2.imread(img_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    try:
        if model is not None:
            model.eval()
            with torch.no_grad():
                results = model([img_rgb])[0]
                for result in results:
                    # Visualization logic or result processing
                    pass
            st.image(img_rgb, caption="Inference Results")
    except Exception as e:
        st.error(f"Error processing image: {e}")

@st.cache_data 
def load_uploaded_model(model_file):
    try:
        model_ = torch.load(model_file, map_location=torch.device('cpu'))
        model_.eval()
        return model_, None
    except Exception as e:
        return None, str(e)

def get_user_model():
    model_bytes = st.sidebar.file_uploader("Upload a .pt Model File", type=['pt'])
    if model_bytes:
        directory = "uploaded_models"
        model_file = save_uploaded_file(directory, model_bytes)
        loaded_model, error_message = load_uploaded_model(model_file)
        if error_message:
            st.sidebar.error(f"Failed to load model: {error_message}")
        else:
            st.sidebar.success("Model uploaded and loaded successfully!")
            return loaded_model
    return None

def main():
    global model

    st.title("🌟 Friend or Foe Dashboard 🌟")
    st.sidebar.title("🛠 Configuration 🛠")

    model = get_user_model()  # Load the model

    if model:
        img_bytes = st.file_uploader("Upload an image here:", type=['png', 'jpeg', 'jpg'])
        if img_bytes:
            img_file = save_uploaded_file("temp_images", img_bytes)
            image_input(img_file)

if __name__ == "__main__":
    main()
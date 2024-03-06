# Python In-built packages
from pathlib import Path
import PIL
from PIL import Image
# External packages
import streamlit as st

# Local Modules
import settings
import helper

# Setting page layout
st.set_page_config(
    page_title="Friend or Foe Detection using YOLOv8",
    page_icon=":gun:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main page heading
st.title("Friend or Foe Detection using YOLOv8")

# Sidebar
st.sidebar.header("ML Model Config")

# Model Options
model_type = st.sidebar.radio(
    "Select Task", ['Detection', 'Segmentation'])

confidence = float(st.sidebar.slider(
    "Select Model Confidence", 10, 25, 100, 40)) / 100

# Selecting Detection Or Segmentation
if model_type == 'Detection':
    model_path = Path(settings.DETECTION_MODEL)
elif model_type == 'Segmentation':
    model_path = Path(settings.SEGMENTATION_MODEL)

# Load Pre-trained ML Model
try:
    model = helper.load_model(model_path)
except Exception as ex:
    st.error(f"Unable to load model. Check the specified path: {model_path}")
    st.error(ex)

st.sidebar.header("Image/Video Config")
source_radio = st.sidebar.radio(
    "Select Source", settings.SOURCES_LIST)

source_img = None
# If image is selected
if source_radio == settings.IMAGE:
    source_img = st.sidebar.file_uploader(
        "Choose an image...", type=("jpg", "jpeg", "png", 'bmp', 'webp'))

#-----------------------------------------------------------------
    # Display the cover image by default
    try:
        cover_image_path = str(settings.COVER_IMAGE)
        cover_image = Image.open(cover_image_path)
        st.image(cover_image, caption="Cover Image", use_column_width=True)
    except Exception as ex:
        st.error("Error occurred while opening the cover image.")
        st.error(ex)

    # When an image is uploaded and the 'Detect Objects' button is pressed
    if source_img is not None and st.sidebar.button('Detect Objects'):
        try:
            uploaded_image = Image.open(source_img)
            st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
            # Process the uploaded image using the model
            res = model.predict(uploaded_image, conf=confidence)
            boxes = res[0].boxes
            res_plotted = res[0].plot()[:, :, ::-1]
            st.image(res_plotted, caption='Detected Image', use_column_width=True)
            with st.expander("Detection Results"):
                for box in boxes:
                    st.write(box.data)
        except Exception as ex:
            st.error("Error occurred while detecting objects.")
            st.error(ex)
#------------------------------------------------------------------


elif source_radio == settings.VIDEO:
        helper.play_stored_video(confidence, model)

elif source_radio == settings.WEBCAM:
    helper.play_webcam(confidence, model)

elif source_radio == settings.RTSP:
    helper.play_rtsp_stream(confidence, model)

elif source_radio == settings.YOUTUBE:
    helper.play_youtube_video(confidence, model)

else:
    st.error("Please select a valid source type!")






# Friend or Foe Detection Web App
The Friend or Foe Detection Web App is a streamlined component of the larger "Friend or Foe" project, designed to leverage the power of YOLOv8 for object detection and segmentation. This web application, built with Streamlit, offers an intuitive interface for users to perform object detection on various media sources, including images, videos, webcams, RTSP streams, and YouTube videos. The app provides customizable settings such as model confidence levels and choice between detection and segmentation tasks.

## Features
- **Customizable Object Detection and Segmentation:** Choose between detection and segmentation modes to suit your specific needs.
- **Flexible Source Options:** Upload images or choose from video, webcam, RTSP stream, or YouTube video inputs for object detection.
Adjustable Model Confidence: Fine-tune the confidence threshold of the model to optimize detection accuracy.
- **Interactive User Interface:** A user-friendly web interface powered by Streamlit, making it accessible to users with varying levels of technical expertise.
- **Real-Time Processing:** Supports real-time object detection and segmentation for video sources including live webcam feeds.

## Getting Started
To use the Friend or Foe Detection Web App, follow these setup instructions:

### Prerequisites
Ensure Python is installed on your system. The app has been tested with Python 3.9 and newer versions.

Installation
1- Clone the Project Repository

Clone the project to your local machine and navigate into the project directory:
```
git clone <repository-url>
cd <project-directory>
```

2- Set Up a Python Virtual Environment (Optional)

It's recommended to use a virtual environment for Python projects. Create and activate one with:

For Windows:
```
python -m venv venv
.\venv\Scripts\activate
```
For macOS/Linux:
```
python3 -m venv venv
source venv/bin/activate
```


3- Install Required Packages
Install the necessary Python packages specified in `app_requirements.txt`:
```
pip install -r app_requirements.txt
```

### Running the Application
Launch the web app using Streamlit with the following command:
```
streamlit run app.py
```


## Usage
Upon launching the web app, you will be presented with a sidebar for configuring the detection settings:

- **Select Task:** Choose between "Detection" and "Segmentation".
- **Model Confidence:** Adjust the slider to set the desired confidence level for the model.
- **Select Source:** Choose your media source for detection (image, video, webcam, RTSP, YouTube).
For image sources, you can upload your image directly. For video sources, input the relevant URL or select from predefined options.

After configuring your settings, initiate the detection process and view the results directly within the web interface.

## Contributing
This web app is part of a larger project, and contributions are welcome. Please refer to the main project documentation for guidelines on contributing.

## License
The Friend or Foe Detection Web App and the larger "Friend or Foe" project are open-source initiatives. Please review the LICENSE file in the main project repository for more information on the terms of use.

## Acknowledgments
- The development of this web app was made possible by the use of the YOLOv8 model from Ultralytics.
- Streamlit has been instrumental in creating an interactive user experience for this application.
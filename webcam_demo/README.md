# Webcam Demo - FFMMMTI

## Overview
To demonstrate the real-time capabilities of our YOLOv8s trained system, we developed a proof-of-concept script that incorporates the CRS code with a Python script designed to perform real-time inference on video streams from the webcam. The AI model seamlessly integrates with the webcam to simulate realistic deployment scenarios. For the Challenge Response aspect, the script leverages the socket connections to allow communication between the sender (soldier aiming down sight) and the receiver (target) thereby emulating the software-defined radio setup. With AI mode enabled, the AI model processes each frame to detect and classify camouflage uniforms as friendly or hostile. The challenge-response system is manually operated where the user issues a command to challenge the target, prompting them to confirm their identity within a short amount of time. Not only does this script showcase the model’s accuracy and robustness, but it also highlights the potential for future integration with external software/hardware components.

## Demo :movie_camera:
![webcam_video_demo_FFMMMTI](https://github.com/Naif-Ganadily/Friend-or-Foe-Multi-Modal-Military-Target-Identification/assets/29029748/90dd5774-6125-4f7c-b484-d7e788ebdb56)

### Prerequisites
The inference package requires Python >=3.8,<=3.11.

## How to run? :computer:
1- Use pip or pip3 to install the modules listed in demo_requirements.txt and docker must be installed. Note, inference server is required for this demo script to run properly. 

2- To run docker, launch Docker Desktop application

3- Open a command terminal (powershell/zsh) then enter one of the following commands depending on your system and the resources you wish to utilize:
```
docker run -it --net=host roboflow/roboflow-inference-server-cpu:latest
docker run -it --network=host --gpus=all roboflow/roboflow-inference-server-gpu:latest
```

You should see similar output to this: 
``` 
INFO:     Started server process [6]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:9001
```

For more information on Roboflow Inference, please refer to this repo ``` https://github.com/roboflow/inference/tree/main ```

4- In another terminal, run the Python script and use the flow diagram as a guide to enable AI and CRS modes.

NOTE: You may need to export the Roboflow private key :key:. Here is how it can be done on the terminal: 
```
export ROBOFLOW_API_KEY=<YOUR_API_KEY>
```

## Usage
- `A` key press: Enables AI mode. In this mode, each webcam video frame is processed to detect US and Russian military soldiers. 
- `C` key press: Enables Challenge Response Mode if and only if AI mode is enabled. In this mode, the challenge response server launches in a separate thread where a socket is opened for 20 seconds. The server will evaluate the payload received on the socket to determine if response is "Friendly" or "Unknown".
- `U` key press: Sends an unknown or non-friendly payload to the challenge response server when Challenge Response mode is enabled. 
- `F` key press: Sends a friendly payload to the challenge response server when Challenge Response mode is enabled. 

NOTE: Ensure the webcam stream window is in focus.

## Flow Diagram 📚
![FlowDiagram_WebcamDemo drawio](https://github.com/Naif-Ganadily/Friend-or-Foe-Multi-Modal-Military-Target-Identification/assets/29029748/401c1fcc-d740-40aa-9f0d-2adfae329804)


## License
The "Friend or Foe" project is an open-source initiative. Please review the LICENSE file in the main project repository for more information on the terms of use.

## Acknowledgments
- The development of this web app was made possible by the use of the YOLOv8 model from Ultralytics and Inference package from Roboflow. 
## Friend or Foe - Multi-Modal Military Target Identification Webcam Demo Script

## Demo :movie_camera:
![webcam_video_demo](https://github.com/Naif-Ganadily/Friend-or-Foe-Multi-Modal-Military-Target-Identification/assets/29029748/72592ca6-23e7-4f08-81c1-e2fccd30b905)

## Flow Diagram 
![FlowDiagram_WebcamDemo drawio](https://github.com/Naif-Ganadily/Friend-or-Foe-Multi-Modal-Military-Target-Identification/assets/29029748/401c1fcc-d740-40aa-9f0d-2adfae329804)

## How to run? 
First, use pip or pip3 to install the modules listed in demo_requirements.txt and docker must be installed. Note, inference server is required for this demo script to run properly. To run docker, launch Docker Desktop application and open a command terminal (powershell/zsh) then enter one of the following commands depending on your system and the resources you wish to utilize:
'''
docker run -it --net=host roboflow/roboflow-inference-server-cpu:latest
docker run -it --network=host --gpus=all roboflow/roboflow-inference-server-gpu:latest
'''

You should see similar output to this: 
'''
INFO:     Started server process [6]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:9001
'''

In another terminal, run the Python script and use the flow diagram as a guide to enable AI and CRS modes.

NOTE: 
You may need to export the Roboflow private key. Here is how it can be done on the terminal: 
'''
export ROBOFLOW_API_KEY=<YOUR_API_KEY>
'''

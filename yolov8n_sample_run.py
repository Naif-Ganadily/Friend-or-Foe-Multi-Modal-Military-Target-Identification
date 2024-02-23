from ultralytics import YOLO
import torch



if __name__ == '__main__':
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


    # Load a model
    model = YOLO("yolov8n.yaml")  # build a new model from scratch

    # Use the model
    model.train(data="config.yaml", epochs=30)  # train the model



# yolov8n-seg.yaml






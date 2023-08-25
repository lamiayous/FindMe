from ultralytics import YOLO
import os

class ObjectDetector:
    def __init__(self, weights="best.pt"):
        model_pth = os.path.join("object_detector", weights)
        self.model = YOLO(model_pth)

    def run_inference(self, img_file): 
        out = self.model.predict(img_file)[0]
        return out
    
from ultralytics import YOLO
import os

class ObjectDetector:
    def __init__(self, weights="best.pt"):
        model_pth = os.path.join("object_detector", weights)
        self.model = YOLO(model_pth)

    def run_inference(self, img_file): 
        out = self.model.predict(img_file)[0]
        return out
    
    def name_of_class(self, results, model):
        names = model.names
        for r in results:
            object_name = names[int(r.boxes.cls)]
        return object_name
    
    def crop_image(self, object_name):
        img_filepath = "./imgs/test/" + object_name
        if os.path.exists(img_filepath) == False:
            os.makedirs(img_filepath)
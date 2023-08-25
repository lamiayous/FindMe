from ultralytics import YOLO
import os
from PIL import Image

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
    
    def crop_image(self, object_name, img_file, result):
        img_filepath = "./imgs/test/" + object_name
        if os.path.exists(img_filepath) == False:
            os.makedirs(img_filepath)
        

        #getting co-ordinates for bounding boxes
        img = Image.open(img_file)
        box = result.boxes[0]
        cords = box.xyxy[0].tolist()
        x1, y1, x2, y2 = cords
        print("Coordinates:", x1)
        img_res = img.crop((x1, y1, x2, y2)) 
        img_res.show() 
        img.show()
import argparse 
import cv2
import os
from ultralytics import YOLO
from autoencoder_inference import encoder_code

class ObjectDetector:
    def __init__(self, weights="best.pt"):
        model_pth = os.path.join("object_detector", weights)
        self.model = YOLO(model_pth)

    def to_dict(self, prediction_output):
        out_dict = {}
        # {0: []} 


    def run_inference(self, img_file): 
        out = self.model.predict(img_file)[0]
        return self.to_dict(out)# , save=False) 
    


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", type=str, default=None)
    args = parser.parse_args() 

    print(args.image)
    img_file =args.image
    img = cv2.imread(img_file)
    object_detector = ObjectDetector()
    out_object_detector = object_detector.run_inference(img_file)
    
    # print(out.boxes)

    ######encoder#######
    encoder_code("last.pth")

if __name__ == "__main__":
    main()
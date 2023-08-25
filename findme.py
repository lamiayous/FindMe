import argparse 
import cv2
import os
from ultralytics import YOLO
from autoencoder_inference import encoder_code
from objectdetector_code import ObjectDetector
    
def main():
    model = YOLO("best.pt")
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", type=str, default=None)
    args = parser.parse_args() 

    img_file =args.image
    object_detector = ObjectDetector()
    out_object_detector = object_detector.run_inference(img_file)
    result = out_object_detector[0]
    names = model.names

    for r in result:
        object_name = names[int(r.boxes.cls)]

    print(object_name)

    ######encoder#######
    encoder_code("last.pth")

if __name__ == "__main__":
    main()
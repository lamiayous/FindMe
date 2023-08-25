import argparse 
import cv2
import os
from ultralytics import YOLO
from autoencoder_inference import encoder_code
from objectdetector_code import ObjectDetector

def main():

    #loading model
    model = YOLO("best.pt")

    #parse from command line 
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", type=str, default=None)
    args = parser.parse_args() 
    img_file =args.image

    ###### Object Detector #######
    object_detector = ObjectDetector()
    out_object_detector = object_detector.run_inference(img_file)
    result = out_object_detector[0]
    
    #extracting name of detected class
    object_name = object_detector.name_of_class(result, model)

    ###### Encoder #######
    encoder_code("last.pth")

if __name__ == "__main__":
    main()
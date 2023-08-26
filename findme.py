import argparse 
from ultralytics import YOLO
from autoencoder_inference import encoder_code
from objectdetector_code import ObjectDetector
from code_construction import test_image_reconstruction
from db import database_upload

def main():
    model = YOLO("best.pt") #loading model

    #parse from command line 
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", type=str, default=None)
    args = parser.parse_args() 
    img_file =args.image

    ###### Object Detector #######
    object_detector = ObjectDetector()
    out_object_detector = object_detector.run_inference(img_file)
    object_detector.object_exist(out_object_detector)

    #extracting name of detected class
    result = out_object_detector[0]
    object_name = object_detector.name_of_class(result, model) #getting object name
    object_detector.crop_image(object_name, img_file, result) #cropping detected image

    ####### Encoder #######
    unique_code = encoder_code("last.pth")

    ###### Database ######
    database_upload(object_name, unique_code)

if __name__ == "__main__":
    main()
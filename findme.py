from parse import parser_img
from ultralytics import YOLO
from autoencoder_inference import encoder_code
from objectdetector_code import ObjectDetector
from code_construction import test_image_reconstruction
from db import database_upload

def main():
    model = YOLO("best.pt") #loading model

    #extracting image from command line
    upload, query = parser_img()
    
    #Checking which mode to use 
    if upload != None:
        img_file = upload

    if query != None:
        object_name = query[0]
        img_file =  query[1]

    ###### Object Detector #######

    object_detector = ObjectDetector()
    out_object_detector = object_detector.run_inference(img_file) #runnning inference
    no_object_detected = len(out_object_detector.boxes) #how many objects are detected

    if no_object_detected == 0: 
        print("No object has been detected, try another image")

    else:
        for object in range(no_object_detected):
            result = out_object_detector[object] #result of detected object (dictionary)
            if upload != None:
                object_name = object_detector.name_of_class(result, model) #getting object name (only in upload mode)
            object_detector.crop_image(object_name, img_file, result) #cropping detected image

            ####### Encoder #######
            unique_code = encoder_code("last.pth")

            ###### Database ######
            if upload != None:
                database_upload(object_name, unique_code) # (only in upload mode)

if __name__ == "__main__":
    main()
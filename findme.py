from ultralytics import YOLO
from parse import parser_img
from autoencoder_inference import encoder_code
from objectdetector_code import ObjectDetector
from db import database_upload
from db import database_query

def main():
    model = YOLO("best.pt") #loading model

    upload, query = parser_img() # extracting image from command line
    
    #Checking which mode to use 
    if upload != None:
        img_file = upload

    if query != None:
        object_name = query[0]
        img_file =  query[1]

    object_detector = ObjectDetector()
    out_object_detector = object_detector.run_inference(img_file) #runnning inference
    no_object_detected = len(out_object_detector.boxes) #how many objects are detected

    if no_object_detected == 0: 
        print("No object has been detected, try another image")

    else:
        if upload != None:
            for object in range(no_object_detected):
                result = out_object_detector[object] #result of detected object (dictionary)
                object_name = object_detector.name_of_class(result, model) #getting object name (only in upload mode)
                object_detector.crop_image(object_name, img_file, result) #cropping detected image
                unique_code = encoder_code("last.pth")
                database_upload(object_name, unique_code) # (only in upload mode)

        if query != None:
            result = out_object_detector[0] #result of detected object (dictionary)
            object_detector.crop_image(object_name, img_file, result) #cropping detected image and storing into file
            unique_code = encoder_code("last.pth") 
            database_query(unique_code)

if __name__ == "__main__":
    main()
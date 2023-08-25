import argparse 
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

    if len(out_object_detector) == 0:
        print("no object detected")
        exit()

    #extracting name of detected class
    result = out_object_detector[0]
    object_name = object_detector.name_of_class(result, model)
    object_detector.crop_image(object_name, img_file, result)
    
    # ###### Encoder #######
    encoder_code("last.pth")

if __name__ == "__main__":
    main()

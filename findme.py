import argparse 
import cv2
import os
from ultralytics import YOLO

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
    # cv2.imshow("image", img)
    # cv2.waitKey()

    object_detector = ObjectDetector()
    out_object_detector = object_detector.run_inference(img_file)
    
    # print(10*"=", out)
    # print(type(out))
    # print(len(out))
    # print(type(out[0]))
    print(out.boxes)
    # print(type(out[0].names))
    # print(type(out[0].keys[0]))

    auto_encoder +
    # for elm in out[0]:
    #     print("element : ", elm)




if __name__ == "__main__":
    main()
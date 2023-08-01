from ultralytics import YOLO

model = YOLO('best.pt')  # load a custom model

results = model('car.jpg', save=True) 
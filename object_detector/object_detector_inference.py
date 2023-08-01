from ultralytics import YOLO

model = YOLO('best.pt')  # load a custom model

results = model('landscape.jpg', save=True) 
from ultralytics import YOLO

num = input("What is the train folder numer? ")

model = YOLO(f'runs/detect/train{num}/weights/best.pt')  # load a custom trained model

# Export the model
model.export(format='edgetpu')
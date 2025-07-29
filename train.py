import os
from ultralytics import YOLO

current_directory = os.path.dirname(os.path.abspath(__file__))
data_yaml_path = os.path.join(current_directory, 'data.yaml')

model = YOLO('yolov8n.pt')

if __name__ == '__main__':
    results = model.train(
        data=data_yaml_path,
        epochs=50,
        imgsz=640,
        device=0,
        name='banknote_yolov8n_results'
    )
import os
import cv2
from ultralytics import YOLO

current_directory = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_directory, 'best.pt')

if not os.path.exists(model_path):
    print(f"Hata: Model dosyasi bulunamadi! -> '{model_path}'")
    exit()

try:
    model = YOLO(model_path)
except Exception as e:
    print(f"Hata: Model yuklenemedi!: {e}")
    exit()

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Hata: Webcam acilamadi.")
    exit()

print("Webcam acildi. Kapatmak icin 'q' tusuna basin.")

while True:
    success, frame = cap.read()
    if not success:
        break

    results = model(frame, conf=0.5)
    annotated_frame = results[0].plot()

    cv2.imshow("YOLOv8 Gercek Zamanli Para Tanima", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
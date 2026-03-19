import cv2
from ultralytics import YOLO

# Load YOLO model
model = YOLO("models/yolov8n.pt")

# Vehicle classes from COCO dataset
vehicle_classes = [2, 3, 5, 7]  
# 2 = car, 3 = motorcycle, 5 = bus, 7 = truck


def detect_vehicles(frame):

    results = model(frame)

    vehicle_boxes = []
    vehicle_count = 0

    for r in results:
        boxes = r.boxes

        for box in boxes:

            cls = int(box.cls[0])

            if cls in vehicle_classes:

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                vehicle_boxes.append((x1, y1, x2, y2))
                vehicle_count += 1

    return vehicle_boxes, vehicle_count
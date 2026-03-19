import cv2
from vehicle_detection import detect_vehicles
from traffic_control import calculate_signal_time

video = cv2.VideoCapture("traffic/traffic.mp4 - Copy.mp4")

while True:

    ret, frame = video.read()

    if not ret:
        break

    boxes, vehicle_count = detect_vehicles(frame)

    # Draw vehicle boxes
    for (x1, y1, x2, y2) in boxes:

        cv2.rectangle(frame,
                      (x1, y1),
                      (x2, y2),
                      (0,255,0),
                      2)

    # Calculate signal time
    signal_time = calculate_signal_time(vehicle_count)

    # Display vehicle count
    cv2.putText(frame,
                f"Vehicle Count: {vehicle_count}",
                (20,40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0,0,255),
                2)

    # Display signal time
    cv2.putText(frame,
                f"Green Signal Time: {signal_time} sec",
                (20,80),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255,0,0),
                2)

    cv2.imshow("Smart Traffic AI", frame)

    if cv2.waitKey(1) == 27:
        break

video.release()
cv2.destroyAllWindows()
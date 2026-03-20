from flask import Flask, Response
import cv2
from vehicle_detection import detect_vehicles
from traffic_control import calculate_signal_time

app = Flask(__name__)

def generate_frames():
    video = cv2.VideoCapture("traffic/traffic.mp4 - Copy.mp4")

    while True:
        success, frame = video.read()
        if not success:
            break

        boxes, vehicle_count = detect_vehicles(frame)

        for (x1, y1, x2, y2) in boxes:
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)

        signal_time = calculate_signal_time(vehicle_count)

        cv2.putText(frame, f"Vehicle Count: {vehicle_count}", (20,40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

        cv2.putText(frame, f"Green Signal Time: {signal_time} sec", (20,80),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
import cv2
from ultralytics import YOLO
import serial
import time

# Konfigürasyon
arduino_port = 'COM8'
baud_rate = 9600
cm_constant = 40000
send_interval = 0.3

ser = None
try:
    ser = serial.Serial(arduino_port, baud_rate, timeout=1)
    time.sleep(2)
    print("✅ Bağlantı Başarılı")
except Exception as e:
    print(f"❌ Hata: {e}")

model = YOLO('yolov8n.pt')
cap = cv2.VideoCapture(0)
last_send_time = 0

while True:
    success, img = cap.read()
    if not success: break

    results = model(img, stream=True, classes=[0], verbose=False)

    person_detected = False
    estimated_distance = 999

    for r in results:
        boxes = r.boxes
        for box in boxes:
            person_detected = True
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            box_width = x2 - x1
            if box_width > 0:
                estimated_distance = int(cm_constant / box_width)

            if estimated_distance < 100:
                color = (0, 0, 255)
                status = "TEHLIKE!"
            elif estimated_distance < 200:
                color = (0, 255, 255)
                status = "DIKKAT!"
            else:
                color = (0, 255, 0)
                status = "GUVENLI"

            cv2.rectangle(img, (x1, y1), (x2, y2), color, 3)
            cv2.putText(img, f"{estimated_distance} cm",
                        (x1, y1 - 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
            cv2.putText(img, status,
                        (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    if person_detected:
        if estimated_distance < 100:
            status_text = "DURUM: TEHLIKE!"
            status_color = (0, 0, 255)
        elif estimated_distance < 200:
            status_text = "DURUM: DIKKAT!"
            status_color = (0, 255, 255)
        else:
            status_text = "DURUM: GUVENLI"
            status_color = (0, 255, 0)
    else:
        status_text = "DURUM: Kisi Yok"
        status_color = (255, 255, 255)

    cv2.rectangle(img, (10, 10), (350, 50), (0, 0, 0), -1)
    cv2.putText(img, status_text, (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, status_color, 2)

    # Bluetooth üzerinden Arduino'ya veri gönderimi
    current_time = time.time()
    if ser and ser.is_open and (current_time - last_send_time > send_interval):
        try:
            if person_detected:
                msg = f"<{estimated_distance}>"
                ser.write(msg.encode())
            else:
                ser.write(b"<999>")
            last_send_time = current_time
        except:
            pass

    cv2.imshow("AI Radar", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        if ser: ser.close()
        break

cap.release()
cv2.destroyAllWindows()

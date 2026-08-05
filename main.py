from ultralytics import YOLO
import cv2

# carregar modelo
model = YOLO("yolov8n.pt")

# abrir webcam (ou vídeo)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # correr deteção
    results = model(frame)

    # desenhar resultados
    annotated_frame = results[0].plot()

    # mostrar
    cv2.imshow("People Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

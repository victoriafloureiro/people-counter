import cv2

cap = cv2.VideoCapture(0)

print("A tentar abrir webcam...")

while True:
    ret, frame = cap.read()
    print("Frame capturado:", ret)

    if not ret:
        print("Erro ao abrir webcam")
        break

    cv2.imshow("Teste", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

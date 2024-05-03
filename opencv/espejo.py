import cv2
import numpy

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret: break
    mitad = frame.shape[1]//2
    frame[:,:mitad] = cv2.flip(frame[:,mitad:], 1)
    cv2.imshow("mirror", frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"): break

cap.release()
cv2.destroyAllWindows()
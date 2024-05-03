import cv2
import numpy

video = cv2.VideoCapture(0)

i = 0
movement = False

while video.isOpened():

    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if not ret: break
    
    if i == 20:
        bgGray = gray
    if i > 20: 
        fps = video.get(cv2.CAP_PROP_FPS)
        cv2.putText(frame, f"FPS: {fps} ciclos: {i//10}x10", (10, 10), cv2.FONT_HERSHEY_COMPLEX, .3, (0,255,0), 1)
        dif = cv2.absdiff(gray, bgGray)
        _, th = cv2.threshold(dif, 10, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for c in contours:
            area = cv2.contourArea(c)
            if area >= 3000:
                x, y, w, h = cv2.boundingRect(c)
                cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

        cv2.imshow("Cámara", frame)
        # cv2.imshow("Binary", th)
    i += 1
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
video.release()
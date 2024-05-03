import cv2
import numpy as np
import imutils
capture = cv2.VideoCapture(0)

def DetectColor(mask,color):
    contours,_ = cv2.findContours(mask,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        area = cv2.contourArea(c)
        
        if area > 3000:
            x, y, w, h = cv2.boundingRect(c)
            marked = imutils.resize(frame[y:y+h, x:x+w], width=300)
            # Dibujar un círculo en el centroide
            xCenter = x+ w//2
            yCenter = y+ h//2
            cv2.circle(frame, (xCenter, yCenter), 5, (0, 255, 0), -1)
            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
            cv2.putText(frame, "{},{}".format(xCenter,yCenter), (xCenter + 10, yCenter), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 1)
            cv2.imshow("roi", marked)

lowerBlue = np.array([100, 100, 20], np.uint8)
upperBlue = np.array([130, 255, 255], np.uint8)

lowerGreen = np.array([40, 40, 40], np.uint8)
upperGreen = np.array([80, 255, 255], np.uint8)

# el color rojo es un color que abarca desde 0 a 10 y de 170 a 179 por eso se usan dos lower y dos upper
lowerRed1 = np.array([0, 100, 20], np.uint8)
upperRed1 = np.array([5, 255, 255], np.uint8)
lowerRed2 = np.array([175, 100, 20], np.uint8)
upperRed2 = np.array([179, 255, 255], np.uint8)

while capture.isOpened():
    ret, frame = capture.read()
    if ret:
        frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        maskBlue = cv2.inRange(frameHSV, lowerBlue, upperBlue)
        maskGreen = cv2.inRange(frameHSV, lowerGreen, upperGreen)
        maskRed1 = cv2.inRange(frameHSV, lowerRed1, upperRed1)
        maskRed2 = cv2.inRange(frameHSV, lowerRed2, upperRed2)
        maskRed = cv2.add(maskRed1, maskRed2)
        DetectColor(maskBlue, (255,0,0))
        DetectColor(maskGreen, (0,255,0))
        DetectColor(maskRed, (0,0,255))

        cv2.imshow("video", frame)
        # cv2.imshow("mask", mask1)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else: break

capture.release()
cv2.destroyAllWindows()


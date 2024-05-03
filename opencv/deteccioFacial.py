import cv2

cascadeClasiff = cv2.CascadeClassifier('haarcascade_frontalface_default.hml')

imagen = cv2.imread("media/gente.jpeg", 0)

cv2.imshow("Imagen", imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np

# Función para detectar colores azules
def detect_blue_color(image):
    # Convertir la imagen de BGR a HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Definir rango de azul en HSV
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])
    
    # Aplicar la máscara para detectar solo el color azul
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    return mask

# Inicializar la captura de video desde la cámara 0
cap = cv2.VideoCapture(0)

while True:
    # Leer un frame de la cámara
    ret, frame = cap.read()
    
    # Detectar colores azules
    blue_mask = detect_blue_color(frame)
    
    # Mostrar la imagen binarizada
    cv2.imshow('Blue Detection', blue_mask)
    
    # Salir del bucle si se presiona 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la captura de video y cerrar todas las ventanas
cap.release()
cv2.destroyAllWindows()

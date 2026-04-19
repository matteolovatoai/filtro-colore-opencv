import cv2
import numpy as np

image = cv2.imread("mela.jpg")

if image is None:
    print("❌ Errore nella lettura dell'immagine")
else:
    # conversione delle immagini in HSV per il filtro colore
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # conversione in grigio per lo sfondo in bianco e nero
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # conversione da grigio a colore per avere i 3 canali per poter riaggiungere la foto successivamente
    image_gray_3c = cv2.cvtColor(image_gray, cv2.COLOR_GRAY2BGR)
    # il rosso è sia all'inizio che alla fine dello spettro hsv quindi devo fare 2 maschere
    # creo i limiti inferiore e superiore per il rosso-arancio
    limit_inf_1 = np.array([0, 100, 100])
    limit_sup_1 = np.array([10, 255, 255])
    # creo i limiti per il rosso-viola
    limit_inf_2 = np.array([160, 100, 100])
    limit_sup_2 = np.array([180, 255, 255])
    # creo le 2 maschere
    mask_1 = cv2.inRange(image_hsv, limit_inf_1, limit_sup_1)
    mask_2 = cv2.inRange(image_hsv, limit_inf_2, limit_sup_2)

    # unisco le maschere
    mask = cv2.bitwise_or(mask_1, mask_2)
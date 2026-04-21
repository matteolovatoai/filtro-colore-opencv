import cv2
import numpy as np

image_name = "mela" # l'immagine si chiama mela.jpg

image = cv2.imread(f"{image_name}.jpg")

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
    limit_inf_1 = np.array([0, 150, 150])
    limit_sup_1 = np.array([6, 255, 255])
    # creo i limiti per il rosso-viola
    limit_inf_2 = np.array([160, 100, 0])
    limit_sup_2 = np.array([179, 255, 255])
    # creo le 2 maschere
    mask_1 = cv2.inRange(image_hsv, limit_inf_1, limit_sup_1)
    mask_2 = cv2.inRange(image_hsv, limit_inf_2, limit_sup_2)

    # unisco le maschere
    mask = cv2.bitwise_or(mask_1, mask_2)
    # creo un "pennello" per passare i bordi
    kernel_cleaning = np.ones((10,10))
    # faccio l'apertura, prima erodo i bordi per mangiare i pixel solitari e poi dilato per tornare alla maschera iniziale, ma pulita
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel_cleaning)
    kernel_closing = np.ones((100,100))
    # faccio il contrario per unire oggetti divisi
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel_closing)

    # creo la maschera inversa per prendere tutto quello che non è rosso
    mask_inv = cv2.bitwise_not(mask)
    # trovo il colore rosso e lo ritaglio
    image_color_mask = cv2.bitwise_and(image, image, mask=mask)
    cv2.imwrite(f"masked_{image_name}.jpg", image_color_mask)
    # ritaglio tutto quello che non è rosso dall'immagine in grigio
    image_gray_mask = cv2.bitwise_and(image_gray_3c, image_gray_3c, mask=mask_inv)
    cv2.imwrite(f"masked_{image_name}_gray.jpg", image_gray_mask)
    # sommo le 2 immagini per ottenere il risultato
    image_result = cv2.add(image_color_mask, image_gray_mask)

    cv2.imwrite(f"result_{image_name}.jpg", image_result)
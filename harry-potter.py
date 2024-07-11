# Harry Potter'ın Görünmez Pelerini

import cv2
import numpy as np

# Kamerayı açın ve arka planı yakalayın
cap = cv2.VideoCapture(0)
try:
    if not cap.isOpened():
        raise IOError("Kamera açılamadı.")

    # Kameranın ısınması için biraz bekleyin
    cv2.waitKey(1000)

    # Arka planı yakalayın
    ret, background = cap.read()
    if not ret:
        raise IOError("Arka plan resmi yakalanamadı.")

except Exception as e:
    print(f"Hata: {e}")
    cap.release()
    cv2.destroyAllWindows()
    exit()

# Mavi renk tespiti için ayarlanabilir parametreler
lower_blue = np.array([100, 150, 0])
upper_blue = np.array([140, 255, 255])

while True:
    # Kare kare görüntü yakalayın
    ret, frame = cap.read()
    if not ret:
        break

    # Kareyi HSV renk uzayına dönüştürün
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Mavi renk için bir maske oluşturun
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Maskenin tersini alın
    mask_inv = cv2.bitwise_not(mask)

    # Maskeyi kullanarak karenin mavi olmayan bölgelerini çıkarın
    non_blue_areas = cv2.bitwise_and(frame, frame, mask=mask_inv)

    # Arka plandaki mavi bölgeleri maske kullanarak çıkarın
    blue_areas_background = cv2.bitwise_and(background, background, mask=mask)

    # Kareyi mavi olmayan bölgeleri ile arka planın mavi bölgeleri ile birleştirin
    result = cv2.add(non_blue_areas, blue_areas_background)

    # Maske üzerine Gauss bulanıklığı uygulayın (isteğe bağlı)
    # mask = cv2.GaussianBlur(mask, (5, 5), 0)

    # Anahtar talimatlarını görüntüleyin
    cv2.putText(result, "'q' veya 'Esc' tusuna basarak cikis yapabilirsiniz.", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # Sonuç karesini görüntüleyin
    cv2.imshow('Harry Potter\'ın Görünmez Pelerini', result)

    # Döngüyü 'q' veya 'Esc' tuşuna basarak sonlandırın
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q') or key == 27:  # 27 'Esc' tuşunun ASCII değeri
        break

# Kamerayı serbest bırakın ve OpenCV pencerelerini kapatın
cap.release()
cv2.destroyAllWindows()

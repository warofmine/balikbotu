import cv2
import numpy as np
import pyautogui
import os

# Çalışma dizinini kontrol et
print(f"Çalışma dizini: {os.getcwd()}")

# Görüntüyü yükle
template_path = r"c:\Users\PC\Desktop\m2phy\balik\nesne.png"  # Tam dosya yolu
if not os.path.exists(template_path):
    raise FileNotFoundError(f"Dosya bulunamadı: {template_path}")

template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
if template is None:
    raise FileNotFoundError(f"Şablon dosyası yüklenemedi: {template_path}")
w, h = template.shape[::-1]

# Ekran görüntüsü al ve işle
screenshot = pyautogui.screenshot()
screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

# Şablon eşleştirme
result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8  # Eşik değeri (0.8 = %80 eşleşme)
locations = np.where(result >= threshold)

# Eşleşen bölgeleri işaretle
for pt in zip(*locations[::-1]):
    cv2.rectangle(screenshot, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)
    print(f"Nesne bulundu! Koordinatlar: {pt}")

# Görüntüyü göster
cv2.imshow("Ekran Görüntüsü", screenshot)
cv2.waitKey(0)
cv2.destroyAllWindows()
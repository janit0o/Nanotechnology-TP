import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def ImportImage(file_path):
    im = Image.open(file_path).convert("L")
    im_array = np.array(im)
    return im_array

def efficient(hologramme, ordre_zero):
    sum_pixel_holo = np.sum(hologramme)
    sum_pixel_zero = np.sum(ordre_zero)
    Eff = sum_pixel_holo / sum_pixel_zero
    return Eff

eff = []
wavelength = []

for i in range(550, 651, 10):
    wavelength.append(i)
    wavelength_str = str(i)

    file_holo = f"image_{wavelength_str}nm.png"
    file_zero = f"center_{wavelength_str}nm.png"

    hologramme = ImportImage(file_holo)
    ordre_zero = ImportImage(file_zero)

    eff.append(efficient(hologramme, ordre_zero))

plt.figure()
plt.plot(wavelength, eff, marker='o')
plt.xlabel("Longueur d'onde (nm)")
plt.ylabel("Efficacité")
plt.title("Courbe spectrale d’efficacité")
plt.grid(True)
plt.tight_layout()
plt.show()
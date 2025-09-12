import os
from PIL import Image

# KAYNAK ve HEDEF klasörleri
src_folder = "data"  # JPG dosyalarının olduğu klasör
dst_folder = "kesilmis_jpg"  # Kesilmiş dosyaların kaydedileceği klasör
os.makedirs(dst_folder, exist_ok=True)

# Kesilecek alanların koordinatları (sol, üst, sağ, alt)
alan1 = (222, 5, 950, 1026)
alan2 = (970, 5, 1700, 1026)

for fname in os.listdir(src_folder):
	if fname.lower().endswith(".png"):
		path = os.path.join(src_folder, fname)
		with Image.open(path) as img:
			# Alan 1'i kes ve kaydet
			crop1 = img.crop(alan1)
			crop1_path = os.path.join(dst_folder, f"{os.path.splitext(fname)[0]}_alan1.jpg")
			crop1.save(crop1_path, "JPEG")
			# Alan 2'yi kes ve kaydet
			crop2 = img.crop(alan2)
			crop2_path = os.path.join(dst_folder, f"{os.path.splitext(fname)[0]}_alan2.jpg")
			crop2.save(crop2_path, "JPEG")
			print(f"{fname} dosyasından alanlar kesildi ve kaydedildi.")

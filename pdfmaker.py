
import os
from PIL import Image
from natsort import natsorted


# JPG dosyalarının bulunduğu klasör
src_folder = "kesilmis_jpg"  # Kendi klasör adınızı yazın
output_pdf = "output.pdf"    # Oluşacak PDF dosyası

# JPG dosyalarını sıralı şekilde al
jpg_files = natsorted([f for f in os.listdir(src_folder) if f.lower().endswith('.jpg')])

images = []
for fname in jpg_files:
	path = os.path.join(src_folder, fname)
	img = Image.open(path).convert("RGB")
	images.append(img)

if images:
	images[0].save(output_pdf, save_all=True, append_images=images[1:])
	print(f"PDF oluşturuldu: {output_pdf}")
else:
	print("Klasörde jpg dosyası bulunamadı.")

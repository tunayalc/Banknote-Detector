import os
import shutil
import math
import re
from collections import defaultdict

current_directory = os.path.dirname(os.path.abspath(__file__))
source_folder = os.path.join(current_directory, "images_to_label")
chunked_folder = os.path.join(current_directory, "chunked_images")
chunk_size = 100

print(f"Kaynak Klasor: {source_folder}")
print(f"Hedef Ana Klasor: {chunked_folder}\n")

if not os.path.exists(source_folder):
    print(f"HATA: Kaynak klasor bulunamadi! -> {source_folder}")
    exit()

if os.path.exists(chunked_folder):
    shutil.rmtree(chunked_folder)
os.makedirs(chunked_folder, exist_ok=True)
print(f"'{os.path.basename(chunked_folder)}' klasoru olusturuldu.\n")

try:
    all_files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]
except FileNotFoundError:
    print(f"HATA: Kaynak klasor '{source_folder}' bulunamadi.")
    exit()
    
total_files = len(all_files)
if total_files == 0:
    print("Tasinacak resim bulunamadi.")
    exit()

print(f"Toplam {total_files} resim bulundu.\n")
total_parts = math.ceil(total_files / chunk_size)
print(f"Resimler {chunk_size}'lik gruplar halinde {total_parts} klasore ayrilacak.\n")

grouped_files = defaultdict(list)
for filename in all_files:
    match = re.match(r"(\d+)", filename)
    if match:
        class_name = match.group(1)
        grouped_files[class_name].append(filename)

for class_name, files in grouped_files.items():
    total_files_in_class = len(files)
    for i in range(0, total_files_in_class, chunk_size):
        part_number = (i // chunk_size) + 1
        part_folder_name = f"{class_name}-part{part_number}"
        part_folder_path = os.path.join(chunked_folder, part_folder_name)
        os.makedirs(part_folder_path, exist_ok=True)
        
        current_chunk = files[i:i + chunk_size]
        for filename in current_chunk:
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(part_folder_path, filename)
            shutil.copy(source_path, destination_path)
            
print("Tüm islemler basariyla tamamlandi.")
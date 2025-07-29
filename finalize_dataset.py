import os
import shutil
import random

current_directory = os.path.dirname(os.path.abspath(__file__))
source_folder = os.path.join(current_directory, "chunked_images")
output_folder = os.path.join(current_directory, "dataset")

train_ratio = 0.7
valid_ratio = 0.2

print("Veri seti birlestirme ve ayirma islemi baslatiliyor...\n")

if os.path.exists(output_folder):
    shutil.rmtree(output_folder)

for split in ['train', 'valid', 'test']:
    for folder_type in ['images', 'labels']:
        os.makedirs(os.path.join(output_folder, split, folder_type), exist_ok=True)
print(f"'{os.path.basename(output_folder)}' icinde yeni klasor yapisi olusturuldu.\n")

all_image_paths = []
for dirpath, _, filenames in os.walk(source_folder):
    for filename in filenames:
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            all_image_paths.append(os.path.join(dirpath, filename))

image_label_map = {}
for img_path in all_image_paths:
    base_name = os.path.splitext(os.path.basename(img_path))[0]
    label_path = os.path.join(os.path.dirname(img_path), base_name + '.txt')
    if os.path.exists(label_path):
        image_label_map[img_path] = label_path

items = list(image_label_map.items())
random.shuffle(items)
total_items = len(items)

train_end = int(total_items * train_ratio)
valid_end = train_end + int(total_items * valid_ratio)

train_set = items[:train_end]
valid_set = items[train_end:valid_end]
test_set = items[valid_end:]

print(f"Toplam {total_items} etiketli resim bulundu ve bolunuyor:")
print(f" - Egitim Seti (Train): {len(train_set)}")
print(f" - Dogrulama Seti (Valid): {len(valid_set)}")
print(f" - Test Seti (Test): {len(test_set)}\n")

sets = {'train': train_set, 'valid': valid_set, 'test': test_set}
for set_name, file_list in sets.items():
    image_dest_dir = os.path.join(output_folder, set_name, 'images')
    label_dest_dir = os.path.join(output_folder, set_name, 'labels')
    for img_path, label_path in file_list:
        shutil.copy(img_path, image_dest_dir)
        shutil.copy(label_path, label_dest_dir)

print("VERI SETI EGITIME TAMAMEN HAZIR!")
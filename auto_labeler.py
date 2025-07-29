import os
import re
from PIL import Image

current_directory = os.path.dirname(os.path.abspath(__file__))
base_folder = os.path.join(current_directory, "chunked_images")

box_width_ratio = 0.90
box_height_ratio = 0.55

class_map = {'5': 0, '10': 1, '20': 2, '50': 3, '100': 4, '200': 5}

print(f"'{os.path.basename(base_folder)}' klasorundeki resimler etiketleniyor...\n")

for folder_name in os.listdir(base_folder):
    folder_path = os.path.join(base_folder, folder_name)
    if not os.path.isdir(folder_path):
        continue
        
    match = re.match(r"(\d+)", folder_name)
    if not match:
        continue
    
    class_name_from_folder = match.group(1)
    if class_name_from_folder not in class_map:
        continue
    
    class_id = class_map[class_name_from_folder]
    
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            label_filename = os.path.splitext(filename)[0] + '.txt'
            label_path = os.path.join(folder_path, label_filename)
            yolo_data = f"{class_id} 0.5 0.5 {box_width_ratio} {box_height_ratio}\n"
            with open(label_path, 'w') as f:
                f.write(yolo_data)
                
print("Otomatik etiketleme tamamlandi.")
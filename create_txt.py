import os
import shutil
import xml.etree.ElementTree as ET
from PIL import Image
# 1. convert format: from label/train/*.xml to *.txt
# 2. copy raw image file to label/train/ folder
# Load class names from classes.txt
with open('D:/waferData/degas/labelApp/data/predefined_classes.txt', 'r') as f:
    classes = f.read().strip().splitlines()

# Path to the folder containing both images and XML annotations
dataset_dir = 'D:/waferData/degas/label/train/'

# Iterate over all XML files in the dataset directory
for xml_file in os.listdir(dataset_dir):
    if xml_file.endswith('.xml'):
        xml_path = os.path.join(dataset_dir, xml_file)
        tree = ET.parse(xml_path)
        root = tree.getroot()
        
        # Get the image filename and dimensions
        image_filename = root.find('path').text
        
        dest_image_path = os.path.join(dataset_dir, os.path.basename(image_filename))
        
        # Copy the image to the dataset directory (if it doesn't already exist)
        if not os.path.exists(dest_image_path):
            shutil.copy(image_filename, dest_image_path)

        # img_path = os.path.join(dataset_dir, image_filename)
        with Image.open(image_filename) as img:
            width, height = img.size
        
        # Prepare the output .txt file with the same basename as the XML file
        txt_filename = xml_file.replace('.xml', '.txt')
        txt_path = os.path.join(dataset_dir, txt_filename)
        
        with open(txt_path, 'w') as f_out:
            # Iterate over each object in the XML file
            for obj in root.findall('object'):
                cls = obj.find('name').text
                # Check if the class is defined in classes.txt
                if cls not in classes:
                    continue
                cls_id = classes.index(cls)
                bndbox = obj.find('bndbox')
                xmin = float(bndbox.find('xmin').text)
                ymin = float(bndbox.find('ymin').text)
                xmax = float(bndbox.find('xmax').text)
                ymax = float(bndbox.find('ymax').text)
                
                # Convert from VOC format to YOLO format (normalized coordinates)
                x_center = ((xmin + xmax) / 2) / width
                y_center = ((ymin + ymax) / 2) / height
                bbox_width = (xmax - xmin) / width
                bbox_height = (ymax - ymin) / height
                
                # Write the YOLO formatted annotation to the file
                f_out.write(f"{cls_id} {x_center} {y_center} {bbox_width} {bbox_height}\n")

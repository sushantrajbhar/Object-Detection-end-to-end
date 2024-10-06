import cv2
import os
import numpy as np

def draw_polygons(image, label_data):
    for line in label_data:
        if not line.strip():  # Skip empty lines
            continue
        points = list(map(float, line.split()[1:]))  # Skip class ID and convert to float
        points = np.array(points).reshape(-1, 2) * np.array([image.shape[1], image.shape[0]])  # Scale points

        # Create a polygon from points and draw it
        polygon = points.astype(int)
        cv2.polylines(image, [polygon], isClosed=True, color=(0, 255, 0), thickness=2)

def process_images(input_image_folder, input_label_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_image_folder):
        if filename.endswith('.jpg') or filename.endswith('.png'):  # Process only image files
            image_path = os.path.join(input_image_folder, filename)
            label_path = os.path.join(input_label_folder, os.path.splitext(filename)[0] + '.txt')

            # Read the image
            image = cv2.imread(image_path)
            if image is None:
                print(f"Could not read image: {image_path}")
                continue

            # Read the label data
            if os.path.exists(label_path):
                with open(label_path, 'r') as file:
                    label_data = file.readlines()
                
                # Draw polygons on the image
                draw_polygons(image, label_data)

                # Save the modified image
                output_image_path = os.path.join(output_folder, filename)
                cv2.imwrite(output_image_path, image)
                print(f"Processed and saved: {output_image_path}")
            else:
                print(f"No label file found for: {filename}")

# Define input and output directories
input_image_folder = r"Image folder path"
input_label_folder = r"Label folder path"
output_folder = r"Directory for output"  # Change as needed

# Process the images
process_images(input_image_folder, input_label_folder, output_folder)

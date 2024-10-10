import os
import csv

# Paths train 
# image_directory = './dataset/train/images'
# csv_file_path = './dataset/train/ground_truth/train_labels.csv'

# Paths test
image_directory = './dataset/test/images'
csv_file_path = './dataset/test/ground_truth/train_labels.csv'
# Check if the CSV exists and delete if it does
if os.path.exists(csv_file_path):
    os.remove(csv_file_path)
    print(f"Existing CSV file at {csv_file_path} has been deleted.")

# Create a new CSV file
with open(csv_file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['filename', 'label'])  # Write the header

    # List and process files in the image directory
    for filename in os.listdir(image_directory):
        if filename.endswith((".png", ".jpg", ".jpeg")):  # Filter to include only image files
            label = '0' if 'abnormal' in filename.lower() else '1'  # Assign label based on filename
            writer.writerow([filename, label])  # Write filename and label to CSV

    print(f"CSV file has been created with new data at {csv_file_path}")

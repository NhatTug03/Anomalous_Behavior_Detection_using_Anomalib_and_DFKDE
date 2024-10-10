import os
import shutil
from sklearn.model_selection import train_test_split

# all_images_dir = './images'
# base_dir = './dataset'
# images = [f for f in os.listdir(all_images_dir)]

# # Split data into training and testing sets
# train_images, test_images = train_test_split(images, test_size=0.2, random_state=42)

# # Function to move files
# def move_files(file_list, source_dir, target_dir):
#     for file_name in file_list:
#         shutil.move(os.path.join(source_dir, file_name), os.path.join(target_dir, file_name))
#         print(f"Moved {file_name} to {target_dir}")

# # Move files to the appropriate directories
# move_files(train_images, all_images_dir, os.path.join(base_dir, 'train/images'))
# move_files(test_images, all_images_dir, os.path.join(base_dir, 'test/images'))


# Example: Assuming all images are initially in a single folder
all_images_dir = "./images"
base_dir = "./dataset2"
images = [f for f in os.listdir(all_images_dir)]

normal_images = []
abnormal_images = []

for filename in images:
    if "abnormal" in filename.lower():
        abnormal_images.append(filename)
    else:
        normal_images.append(filename)


# Function to copy files
def copy_files(file_list, source_dir, target_dir):
    for file_name in file_list:
        shutil.copy(
            os.path.join(source_dir, file_name), os.path.join(target_dir, file_name)
        )
        print(f"Copied {file_name} to {target_dir}")


# Copy files to the appropriate directories
copy_files(normal_images, all_images_dir, os.path.join(base_dir, "good"))
copy_files(abnormal_images, all_images_dir, os.path.join(base_dir, "crack"))

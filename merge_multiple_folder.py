import os
import shutil

source_directory = "./DATA"
destination_directory = "./images"


def is_image(filename):
    image_extensions = [".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff"]
    return any(filename.lower().endswith(ext) for ext in image_extensions)


for subdir, dirs, files in os.walk(source_directory):
    for file in files:
        file_path = os.path.join(subdir, file)
        if is_image(file_path):
            # Construct the path to where the file will be saved
            destination_path = os.path.join(
                destination_directory, os.path.basename(file)
            )
            # Check if the file already exists and generate a new name if necessary to avoid overwrites
            if os.path.exists(destination_path):
                base, extension = os.path.splitext(destination_path)
                i = 1
                # Generate a new file name until it doesn't exist
                while os.path.exists(f"{base}_{i}{extension}"):
                    i += 1
                destination_path = f"{base}_{i}{extension}"
            # Copy the file
            shutil.copy(file_path, destination_path)
            print(f"Copied '{file}' to '{destination_path}'")

import os

# # Define the base directory for the dataset
# base_dir = './dataset'

# # Define subdirectories
# sub_dirs = ['train/images', 'train/ground_truth', 'test/images', 'test/ground_truth']

# # Create the directory structure
# for sub_dir in sub_dirs:
#     # Construct the directory path
#     dir_path = os.path.join(base_dir, sub_dir)

#     # Make the directory if it does not exist
#     os.makedirs(dir_path, exist_ok=True)
#     print(f"Created directory {dir_path}")

# Define the base directory for the dataset
base_dir = "./dataset2"

# Define subdirectories
sub_dirs = ["good", "crack", "mask/crack"]

# Create the directory structure
for sub_dir in sub_dirs:
    # Construct the directory path
    dir_path = os.path.join(base_dir, sub_dir)

    # Make the directory if it does not exist
    os.makedirs(dir_path, exist_ok=True)
    print(f"Created directory {dir_path}")

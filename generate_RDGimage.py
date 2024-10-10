import cv2
import numpy as np
import os
from generate_pairfiles import paired_files
base_dir = './DATA'

def assign_label(prefix):
    """Assigns label based on the presence of a substring in the prefix."""
    return 'normal' if 'binh_thuong' in prefix else 'abnormal'

for prefix, file_list in paired_files.items():
    print(f"Processing videos for prefix: {prefix}")
    # Create a directory for each prefix if it doesn't exist
    prefix_dir = os.path.join(base_dir, prefix)
    if not os.path.exists(prefix_dir):
        try:
          os.makedirs(prefix_dir)
          print(f"Created directory {prefix_dir}")
        except OSError as e:
          print(f"Error creating directory {prefix_dir}: {e.strerror}")

    # Construct full file paths for RGB and Depth videos
    rgb_path = os.path.join(base_dir, file_list[0])
    depth_path = os.path.join(base_dir, file_list[1])

    # Open video captures
    cap_rgb = cv2.VideoCapture(rgb_path)
    cap_depth = cv2.VideoCapture(depth_path)

    if not cap_rgb.isOpened() or not cap_depth.isOpened():
        print(f"Error opening video files for {prefix}")
        continue

    frame_id = 0
    while True:
        ret_rgb, frame_rgb = cap_rgb.read()
        ret_depth, frame_depth = cap_depth.read()

        if not ret_rgb or not ret_depth:
            break

        # Convert depth to grayscale assuming it's in BGR format
        depth_gray = cv2.cvtColor(frame_depth, cv2.COLOR_BGR2GRAY)

        # Merge channels to form RDG
        rdg_frame = cv2.merge((frame_rgb[:, :, 0], depth_gray, frame_rgb[:, :, 1]))

        # Assign a label based on the prefix
        label = assign_label(prefix)

        # Construct filename with unique frame ID and label
        frame_filename = f'{prefix}_rdg_frame_{frame_id}_{label}.png'
        full_path = os.path.join(prefix_dir, frame_filename)

        # Save RDG frame
        cv2.imwrite(full_path, rdg_frame)
        print(f"Saved {full_path} with label {label}")
        frame_id += 1

    # Release video captures
    cap_rgb.release()
    cap_depth.release()

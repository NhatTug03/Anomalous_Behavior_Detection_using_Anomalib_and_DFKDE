import os
# Đường dẫn tới file trong Google Drive
folder_path = './DATA'

# Liệt kê các file trong thư mục
files = os.listdir(folder_path)
for file in files:
    print(file)
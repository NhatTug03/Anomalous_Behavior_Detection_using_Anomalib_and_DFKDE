from check_filename import files


paired_files = {}
for file in files:
    prefix = file.split('(')[0]  # Lấy tiền tố trước dấu ngoặc
    if prefix not in paired_files:
        paired_files[prefix] = []
    paired_files[prefix].append(file)

# Hiển thị các file đã được gom nhóm
for prefix, file_list in paired_files.items():
    print(f"{prefix}: {file_list}")
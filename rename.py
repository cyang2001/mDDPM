import os
import glob

old_path = r"./raw_Data/Brats21/BraTS2021_*" # 旧的文件路径
new_path = r"./raw_Data/Brats21/t2" # 新的文件路径

if not os.path.exists(new_path):
    os.makedirs(new_path)

files = glob.glob(os.path.join(old_path,"*t2.nii.gz")) # 读取旧路径下的nii文件
echo = f"Total {len(files)} files found in {old_path}"
print(echo)
for i, file in enumerate(files, start=1):
    new_filename = f"Brats{i}_t2.nii.gz" # 新的文件名
    new_file_path = os.path.join(new_path, new_filename) # 新的文件路径

    os.rename(file, new_file_path) # 移动并重命名文件
    echo = f"File {file} has been renamed to {new_file_path}"
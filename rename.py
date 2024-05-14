import os
import glob

path = r"/home/pc/Documents/DDPMs/mDDPM/raw_Data/IXI/t2" # 数据读取目录

images = glob.glob(os.path.join(path,"*.nii.gz")) # 读取path下的nii文件
for i, image in enumerate(images, start=1):
    new_filename = f"IXI{i}.nii.gz" # 新的文件名
    new_path = os.path.join(path, new_filename) # 新的文件路径

    os.rename(image, new_path) # 重命名文件
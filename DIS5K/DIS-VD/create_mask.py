import cv2
import numpy as np
import os

# 指定源文件夹和目标文件夹
source_folder = '未命名文件夹'
target_folder = 'mask'

# 确保目标文件夹存在
if not os.path.exists(target_folder):
    os.makedirs(target_folder)

# 遍历源文件夹中的所有文件
for filename in os.listdir(source_folder):
    if filename.endswith('.png'):
        # 构建完整的文件路径
        file_path = os.path.join(source_folder, filename)
        # 读取图片
        img = cv2.imread(file_path, cv2.IMREAD_UNCHANGED)
        
        # 检查图片是否具有透明通道
        if img.shape[2] == 4:
            # 遍历图片的每个像素
            for i in range(img.shape[0]):
                for j in range(img.shape[1]):
                    # 获取像素值
                    b, g, r, a = img[i, j]
                    # 如果像素不透明
                    if a != 0:
                        # 将像素改为白色
                        img[i, j] = (0, 0, 0, 255)
                    else:
                        # 将像素改为白色
                        img[i, j] = (255, 255, 255, 255)
            # 保存修改后的图片
            cv2.imwrite(os.path.join(target_folder, filename), img)
        else:
            print(f"Image {filename} does not have an alpha channel.")

#图片多
import os

image_dir = 'E:\源代码和数据集\基于改进YOLOv5s的鱼苗检测计数设计与实现-数据集和源码\datasets_NEW\images'  # 图像文件夹路径
label_dir = 'E:\源代码和数据集\基于改进YOLOv5s的鱼苗检测计数设计与实现-数据集和源码\datasets_NEW\worktxt'  # 标签文件夹路径
#  
# 获取图像文件夹中的所有文件名
image_files = [f for f in os.listdir(image_dir) if f.endswith('.jpg')]
#  
#获取标签文件夹中的所有文件名
label_files = [f for f in os.listdir(label_dir) if f.endswith('.xml')]
#  
#检查每个图像文件是否有对应的标签文件
for image_file in image_files:
  # 组合图像文件的路径和标签文件的路径
    image_file_path = os.path.join(image_dir, image_file)
    label_file_path = os.path.join(label_dir, image_file.replace('.jpg', '.xml'))
#  
    if not os.path.exists(label_file_path):
        print(f'标签文件 {label_file_path} 不存在与图像文件 {image_file_path} 对应')
print('-------------------------------------------------------------------------------------------------------------')
#标签多
#import os
# 
#image_dir = 'E:\源代码和数据集\基于改进YOLOv5s的鱼苗检测计数设计与实现-数据集和源码\datasets_NEW\images'  # 图像文件夹路径
#label_dir = 'E:\源代码和数据集\基于改进YOLOv5s的鱼苗检测计数设计与实现-数据集和源码\datasets_NEW\worktxt'  # 标签文件夹路径
#
## # 获取图像文件夹中的所有文件名
#image_files = [f for f in os.listdir(image_dir) if f.endswith('.xml')]
# 
## # 获取标签文件夹中的所有文件名
#label_files = [f for f in os.listdir(label_dir) if f.endswith('.jpg')]
# 
###检查每个图像文件是否有对应的标签文件
#for image_file in image_files:
# # #组合图像文件的路径和标签文件的路径
#    image_file_path = os.path.join(image_dir, image_file)
#    label_file_path = os.path.join(label_dir, image_file.replace('.xml', '.jpg'))
# 
#    if not os.path.exists(label_file_path):
#        print(f'图像文件 {label_file_path} 不存在与标签文件 {image_file_path} 对应')
import os

# 图片存放的路径
path_Images = r"D:\MaixPy IDE daima\model_train\maix_train\datasets\egg\images\egg"
path_Txt = r"D:\MaixPy IDE daima\model_train\maix_train\datasets\egg\xml\egg"
start_num = 1
# 遍历更改文件名
num = start_num
for file in os.listdir(path_Images):
    os.rename(os.path.join(path_Images,file),os.path.join(path_Images, "" + str(num))+".jpg")
    num = num + 1

# num = start_num
# for file in os.listdir(path_Txt):
#     os.rename(os.path.join(path_Txt,file),os.path.join(path_Txt, "" + str(num))+".xml")
#     num = num + 1
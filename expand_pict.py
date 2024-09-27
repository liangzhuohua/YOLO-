# -*- coding: utf-8 -*-

import os
import numpy as np
from PIL import Image,ImageChops,ImageEnhance
import cv2
import random

# ========================================翻转=========================================
def image_reversal(img,savefilepath,save_filename):
    """ 图像翻转"""
    lr=img.transpose(Image.FLIP_LEFT_RIGHT) # 左右翻转
    ud=img.transpose(Image.FLIP_TOP_BOTTOM) # 上下翻转
    lr.save(savefilepath+save_filename)
    ud.save(savefilepath+save_filename)

# ========================================旋转=========================================
def image_rotation(img,savefilepath,save_filename):
    """图像旋转"""
    size1 = random.randint(1, 90)
    size2 = random.randint(1, 90)
    out1=img.rotate(size1) # 旋转20度
    out2=img.rotate(size2) # 旋转30度
    out1.save(savefilepath+save_filename)
    out2.save(savefilepath+save_filename)

# ========================================平移=========================================
def image_translation(img,savefilepath,save_filename):
    """图像平移"""
    size = random.randint(1, 90)
    out3=ImageChops.offset(img,size,0) # 只沿X轴平移
    out4=ImageChops.offset(img,0,size) # 只沿y轴平移
    out3.save(savefilepath+save_filename)
    out4.save(savefilepath+save_filename)

# ========================================亮度=========================================
def image_brightness(img,savefilepath,save_filename):
    """亮度调整"""
    size = round(random.uniform(0, 1), 2)
    bri=ImageEnhance.Brightness(img)
    bri_img1=bri.enhance(size) # 小于1为减弱
    bri_img2=bri.enhance(2-size) # 大于1为增强
    bri_img1.save(savefilepath+save_filename)
    bri_img2.save(savefilepath+save_filename)

# ========================================色度=========================================
def image_chroma(img,savefilepath,save_filename):
    """色度调整"""
    size = round(random.uniform(0,1), 2)
    col = ImageEnhance.Color(img)
    col_img1 = col.enhance(size) # 色度减弱
    col_img2 = col.enhance(2-size) # 色度增强
    col_img1.save(savefilepath+save_filename)
    col_img2.save(savefilepath+save_filename)

# ========================================对比度=========================================
def image_contrast(img,savefilepath,save_filename):
    """对比度调整"""
    size = round(random.uniform(0, 1), 2)
    con=ImageEnhance.Contrast(img)
    con_img1=con.enhance(size) # 对比度减弱
    con_img2=con.enhance(2-size) # 对比度增强
    con_img1.save(savefilepath+save_filename)
    con_img2.save(savefilepath+save_filename)


# ========================================锐度=========================================
def image_sharpness(img,savefilepath,save_filename):
    """锐度调整"""
    size = round(random.uniform(0, 1), 2)
    sha = ImageEnhance.Sharpness(img)
    sha_img1 = sha.enhance(size) # 锐度减弱
    sha_img2 = sha.enhance(2-size) # 锐度增强
    sha_img1.save(savefilepath+save_filename)
    sha_img2.save(savefilepath+save_filename)

# ========================================放大缩小=========================================
def image_zoom(img, savefilepath,save_filename):
    """放大缩小"""
    # 打开图片文件
    size = round(random.uniform(0, 1), 2)
    #缩小图像
    img_new1 = img.resize(int(img.size[0]*size), int(img.size[1]*size))

    #放大图像
    img_new2 = img.resize(int(img.size[0]*(2-size)), int(img.size[1]*(2-size)))

    img_new1.save(savefilepath + save_filename)
    img_new2.save(savefilepath + save_filename)

# ========================================高斯白噪声=========================================
def image_white_noise(img, savefilepath,save_filename):
    #将图像转换为Numpy数组
    array = np.asarray(img)

    #生成高斯白噪声
    noise = np.random.normal(0, 10, array.shape).astype('uint8')

    #合并原始图像与高斯白噪声
    result = cv2.addWeighted(array, 0.75, noise, 0.25, 0)

    #创建新的image图像
    img_new = Image.fromarray(result)

    #保存结果图像
    img_new.save(savefilepath + save_filename)

# 定义扩充图片函数
def image_expansion(filepath,savefilepath):
    """
    :param filepath: 图片路径
    :param savefilepath: 扩充保存图片路径
    :param save_prefix: 图片前缀
    :return: 图片扩充数据集
    """
    i = 1

    for parent, dirnames, filenames in os.walk(filepath):
        for filename in filenames:
            image_path=filepath+filename
            print('正在扩充图片：%s' %filename)
            try:
                img=Image.open(image_path)
                if img.mode == "P":
                    img = img.convert('RGB')
                image_reversal(img,savefilepath,save_filename=str(i) + '.jpg')
                i += 1
                image_rotation(img,savefilepath,save_filename=str(i)+'.jpg')
                i += 1
                image_translation(img,savefilepath,save_filename=str(i)+'.jpg')
                i += 1
                image_brightness(img,savefilepath,save_filename=str(i)+'.jpg')
                i += 1
                image_chroma(img,savefilepath,save_filename=str(i)+'.jpg')
                i += 1
                image_contrast(img,savefilepath,save_filename=str(i)+'.jpg')
                i += 1
                image_sharpness(img,savefilepath,save_filename=str(i)+'.jpg')
                i += 1
                image_zoom(img, savefilepath, save_filename=str(i)+'.jpg')
                i += 1
                image_white_noise(img, savefilepath, save_filename=str(i)+'.jpg')
                i += 1
            except Exception as e:
                print(e)
                pass



if __name__ == '__main__':
    # 设置图片路径
    filepath = 'D:/大创/data/rice_leaf_blast'

    # 设置扩充保存图片路径
    savefilepath ='D:/大创/temp'

    image_expansion(filepath, savefilepath)
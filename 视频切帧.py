import cv2
 
vc = cv2.VideoCapture(r"E:\字体识别测试图片\video.mp4")  # 读入视频文件，命名cv（改）
n = 1  # 计数
 
if vc.isOpened():  # 判断是否正常打开
    rval, frame = vc.read()
else:
    rval = False
 
timeF = 4  # 视频帧计数间隔频率(改)
 
i = 132
while rval:  # 循环读取视频帧
    rval, frame = vc.read()
    if (n % timeF == 0):  # 每隔timeF帧进行存储操作
        i += 1
        print(i)
        cv2.imwrite(r"E:\字体识别测试图片\images".format(i), frame)  # 存储为图像（改）
    n = n + 1
    cv2.waitKey(1)
vc.release()

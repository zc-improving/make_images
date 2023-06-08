#encoding=gbk
import glob

import cv2
import os
from pathlib import Path
import glob
def get_img(path):
    abs_path=os.path.realpath('.')
    path=path.replace('./', str(Path(abs_path).parent)+ os.sep)  if path.startswith('./') else path# 当为相对目录时，替换为根目录,其实换不换都可以的
    # print(path)
    video_formats=['mp4','avi']
    video_path=path
    video=[]
    f = []
    # print(os.listdir(video_path))
    if str(video_path).split('.')[-1]  in video_formats:  ##如果参数为特定视频
        f.append(video_path) #
        # print(f)
    elif (Path(video_path)).is_dir():
        # print('s')
        # video_path=Path()

        f+=glob.glob(str(Path(video_path)/'**'/'*.*'),recursive=True) ## 读取目录下所有的文件

        # print(video)
    else:
        video=[]
    video += [x.replace('/',os.sep) for x in f if x.split(".")[-1] in video_formats] ##  匹配video_formats下的格式
    print(video)
    for video_ in video:
        cap = cv2.VideoCapture(video_) # 读入视频文件
        num_frame = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        # print(num_frame)
        # for i in range(num_frame):
        # print(video_)
        file_name=(video_.split('\\')[-1]).split('.')[0]   ##记录文件夹下每一个视频的 name
        folder_name = (video_.split('.')[0])   ##创建每一个视频的保存的文件名字

        os.makedirs(folder_name, exist_ok=True) ##创建保存文件
        if cap.isOpened():  # 判断是否正常打开
            rval, frame = cap.read()
        else:
            rval = False
        timeF = 3  # 视频帧计数间隔频率
        c=1
        while rval:  # 循环读取视频帧
            rval, frame = cap.read()
            pic_path = folder_name + '/'
            if (c % timeF == 0):  # 每隔timeF帧进行存储操作
                cv2.imwrite(pic_path + file_name + '_' + str(c) + '.jpg', frame)  # 存储为图像,保存名为 文件夹名_数字（第几个文件）.jpg
            c = c + 1
            cv2.waitKey(1)
        cap.release()


# print(os.path.abspath(__file__))  # 当前文件所在路径
# print(os.path.realpath("."))  # 当前路径的parent
# print(os.path.abspath(r".."))  # 上一级路径，
# print(os.path.abspath(r"./video_image.py"))  # 一绝对路径
####  上下两个函数一样的
# print(os.path.realpath(__file__))
# print(os.path.realpath(r"."))
# print(os.path.realpath(r".."))
# print(os.path.realpath(r"./video_image.py"))


if __name__ =="__main__":
    path='D:\Project\make_image\\video'
    # print(glob.glob(str(Path(path)/'**')))
    # print(Path(path).parent)
    print(glob.glob(str(Path(path)/'**'/'*'),recursive=True)) # recursive保证**文件和**/*.*文件，搭配着'**'/
    # print(glob.glob(str(Path(path) / '**' / '*.*')))
    # get_img(path=path)
    # print(Path(path).stem)
#
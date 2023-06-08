#encoding=gbk
import glob

import cv2
import os
from pathlib import Path
import glob
def get_img(path):
    abs_path=os.path.realpath('.')
    path=path.replace('./', str(Path(abs_path).parent)+ os.sep)  if path.startswith('./') else path# ��Ϊ���Ŀ¼ʱ���滻Ϊ��Ŀ¼,��ʵ�����������Ե�
    # print(path)
    video_formats=['mp4','avi']
    video_path=path
    video=[]
    f = []
    # print(os.listdir(video_path))
    if str(video_path).split('.')[-1]  in video_formats:  ##�������Ϊ�ض���Ƶ
        f.append(video_path) #
        # print(f)
    elif (Path(video_path)).is_dir():
        # print('s')
        # video_path=Path()

        f+=glob.glob(str(Path(video_path)/'**'/'*.*'),recursive=True) ## ��ȡĿ¼�����е��ļ�

        # print(video)
    else:
        video=[]
    video += [x.replace('/',os.sep) for x in f if x.split(".")[-1] in video_formats] ##  ƥ��video_formats�µĸ�ʽ
    print(video)
    for video_ in video:
        cap = cv2.VideoCapture(video_) # ������Ƶ�ļ�
        num_frame = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        # print(num_frame)
        # for i in range(num_frame):
        # print(video_)
        file_name=(video_.split('\\')[-1]).split('.')[0]   ##��¼�ļ�����ÿһ����Ƶ�� name
        folder_name = (video_.split('.')[0])   ##����ÿһ����Ƶ�ı�����ļ�����

        os.makedirs(folder_name, exist_ok=True) ##���������ļ�
        if cap.isOpened():  # �ж��Ƿ�������
            rval, frame = cap.read()
        else:
            rval = False
        timeF = 3  # ��Ƶ֡�������Ƶ��
        c=1
        while rval:  # ѭ����ȡ��Ƶ֡
            rval, frame = cap.read()
            pic_path = folder_name + '/'
            if (c % timeF == 0):  # ÿ��timeF֡���д洢����
                cv2.imwrite(pic_path + file_name + '_' + str(c) + '.jpg', frame)  # �洢Ϊͼ��,������Ϊ �ļ�����_���֣��ڼ����ļ���.jpg
            c = c + 1
            cv2.waitKey(1)
        cap.release()


# print(os.path.abspath(__file__))  # ��ǰ�ļ�����·��
# print(os.path.realpath("."))  # ��ǰ·����parent
# print(os.path.abspath(r".."))  # ��һ��·����
# print(os.path.abspath(r"./video_image.py"))  # һ����·��
####  ������������һ����
# print(os.path.realpath(__file__))
# print(os.path.realpath(r"."))
# print(os.path.realpath(r".."))
# print(os.path.realpath(r"./video_image.py"))


if __name__ =="__main__":
    path='D:\Project\make_image\\video'
    # print(glob.glob(str(Path(path)/'**')))
    # print(Path(path).parent)
    print(glob.glob(str(Path(path)/'**'/'*'),recursive=True)) # recursive��֤**�ļ���**/*.*�ļ���������'**'/
    # print(glob.glob(str(Path(path) / '**' / '*.*')))
    # get_img(path=path)
    # print(Path(path).stem)
#
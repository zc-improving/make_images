import cv2
import os
import numpy as np
import glob
from pathlib import Path
file_dir='D:\chengxu\mycode\detect_track\\bubble_counting\data\\test'
VIDEO_OUTPUT_PATH='D:\chengxu\mycode\detect_track\\bubble_counting\data\\test/test_.avi'
FPS=30
sz=(640,480)
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')  # opencv3.0
video_writer = cv2.VideoWriter(VIDEO_OUTPUT_PATH, fourcc, FPS, sz, True)
f=[]
img_formats=['jpg','png','bmp']
p = Path(file_dir)
if p.is_dir():  # dir
    f+=glob.glob(str(p / '**' / '*.*'), recursive=True)
# print(f)
f=sorted([x for x in f if x.split('.')[-1].lower() in img_formats] ,key = lambda x: int((x.split('\\')[-1]).split('.')[0]))

# print(f)
# img_files=sorted([x.replace('/', os.sep) for x in f if x.split('.')[-1].lower() in img_formats])
# print(img_files)
print(len(f))
for i in range(len(f)):
    print(i)
    frame=cv2.imread(f[i],flags=1)
    video_writer.write(frame)

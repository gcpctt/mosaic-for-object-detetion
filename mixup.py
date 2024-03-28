import os
import random

import cv2
import numpy as np


img_dir = r"D:\PythonProjects\darklight_data\data\images\train"
txt_dir = r"D:\PythonProjects\darklight_data\data\labels\train"

img_path=[]
txt_path=[]
label=[]

new_img_dir = "mixup_img"
new_txt_dir = "mixup_label"
for img in os.listdir(img_dir):
    random_num = random.uniform(0,1)

    if random_num < 0.05:
        img_path.append(os.path.join(img_dir,img))
        txt_path.append(os.path.join(txt_dir,img.split(".")[0]+".txt"))
        label.append(img.split(".")[0])
        while(len(img_path)==2):
            # 读取图像
            img1 = cv2.imread(img_path[0])
            img2 = cv2.imread(img_path[1])

            new_txt= r"mixup_img.txt"

            with open(txt_path[0],"r") as f:
                data0 = f.readlines()
            with open(txt_path[1],"r") as f:
                data1 = f.readlines()

            data0[-1] = data0[-1]+"\n"
            for data in data1:
                data0.append(data)


            with open(os.path.join(new_txt_dir,label[0]+"_"+label[1]+".txt"), 'w') as f:
                for line in data0:
                    f.write(line.replace(',', '\n'))



            # mixup参数
            lambd = 0.5

            # mixup两张图片
            mix_img = cv2.addWeighted(img1, lambd, img2, 1-lambd, 0)

            # 显示合成后的图片
            cv2.imwrite(os.path.join(new_img_dir,label[0]+"_"+label[1]+".png"), mix_img)

            img_path = []
            txt_path = []
            label = []

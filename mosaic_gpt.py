import os
import random

import cv2
import numpy as np




def process_data(lines, shift_x=0, shift_y=0):
    data_array = []
    for line in lines:
        data = line.strip().split(' ')
        data_float = [int(data[0])] + [float(num)/2 + shift for num, shift in zip(data[1:], (shift_x, shift_y, 0, 0))]
        data_array.append(data_float)
    return data_array

def adjust_position(lines, shift_x=0, shift_y=0):
    data_array = []
    for line in lines:
        data = line.strip().split(' ')
        data_float = [int(data[0])] + [float(num)/2 + shift for num, shift in zip(data[1:], (shift_x, shift_y, 0, 0))]
        data_array.append(data_float)
    return data_array


# 读取图片



def output():
    data_arrays = []
    for txt_path in txt_paths:
        with open(txt_path, "r") as f:
            lines = f.readlines()
        data_arrays.append(lines)

    shifts = [(0, 0), (0.5, 0), (0, 0.5), (0.5, 0.5)]

    with open("demo_.txt", "w") as f:
        for data, shift in zip(data_arrays, shifts):
            adjusted_data = adjust_position(data, *shift)
            for row in adjusted_data:
                row_str = " ".join(str(elm) for elm in row)
                f.write(row_str + "\n")
if __name__ == '__main__':
    # 图片路径
    img_paths = []
    txt_paths = []

    img_dir = r"D:\PythonProjects\darklight\data\images\train"
    label_dir = r"D:\PythonProjects\darklight\data\labels\train"
    label = []

    for img in os.listdir(img_dir):
        random_num = random.uniform(0.0, 1.0)
        if random_num < 0.2857:
            img_paths.append(os.path.join(img_dir, img))
            txt_paths.append(os.path.join(label_dir, img.split(".")[0] + ".txt"))
            label.append(img.split(".")[0])

            while (len(img_paths) == 4):
                images = [cv2.imread(img_path) for img_path in img_paths]
                label_str = "_".join(str(num) for num in label)
                label = []
                # 调整图片大小（缩小为原始尺寸的一半）
                resized_images = [cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2)) for img in images]

                # 创建新的空白图像
                result = 255 * np.ones((resized_images[0].shape[0] * 2, resized_images[0].shape[1] * 2, 3), np.uint8)

                # 将四张图片放置在合成图像中
                for i, img in enumerate(resized_images):
                    row_start = i // 2 * img.shape[0]
                    col_start = (i % 2) * img.shape[1]
                    result[row_start:row_start + img.shape[0], col_start:col_start + img.shape[1]] = img

                img_pth = os.path.join("4img",label_str+".png")
                cv2.imwrite(img_pth, result)

                ## txt
                data_arrays = []
                for txt_path in txt_paths:
                    with open(txt_path, "r") as f:
                        lines = f.readlines()
                    data_arrays.append(lines)

                shifts = [(0, 0), (0.5, 0), (0, 0.5), (0.5, 0.5)]

                with open(os.path.join("4label",label_str+".txt"),"w") as f:
                    for data, shift in zip(data_arrays, shifts):
                        adjusted_data = adjust_position(data, *shift)
                        for row in adjusted_data:
                            row_str = " ".join(str(elm) for elm in row)
                            f.write(row_str + "\n")

                img_paths=[]
                txt_paths=[]


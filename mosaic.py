import cv2
import numpy as np

# 图片路径
img_paths = [
    r"D:\PythonProjects\darklight\data\images\train\3.png",
    r"D:\PythonProjects\darklight\data\images\train\5.png",
    r"D:\PythonProjects\darklight\data\images\train\7.png",
    r"D:\PythonProjects\darklight\data\images\train\9.png"
]

txt_paths = [
    r"D:\PythonProjects\darklight\data\labels\train\3.txt",
    r"D:\PythonProjects\darklight\data\labels\train\5.txt",
    r"D:\PythonProjects\darklight\data\labels\train\7.txt",
    r"D:\PythonProjects\darklight\data\labels\train\9.txt",
]

with open(txt_paths[0],"r") as f:
    line0 = f.readlines()
with open(txt_paths[1],"r") as f:
    line1 = f.readlines()
with open(txt_paths[2],"r") as f:
    line2 = f.readlines()
with open(txt_paths[3],"r") as f:
    line3 = f.readlines()

def left_bottom(lines):
    data_array=[]
    for line in lines:
        data = line.strip().split(' ')
        data_float = [int(data[0])] + [float(num) for num in data[1:]]
        data_array.append(data_float)
    for data in data_array:
        data[1] = data[1]/2
        data[2] = data[2]/2+0.5
        data[3] = data[3]/2
        data[4] = data[4]/2
    return data_array

def right_bottom(lines):
    data_array=[]
    for line in lines:
        data = line.strip().split(' ')
        data_float = [int(data[0])] + [float(num) for num in data[1:]]
        data_array.append(data_float)
    for data in data_array:
        data[1] = data[1]/2+0.5
        data[2] = data[2]/2+0.5
        data[3] = data[3]/2
        data[4] = data[4]/2
    return data_array

def left_top(lines):
    data_array=[]
    for line in lines:
        data = line.strip().split(' ')
        data_float = [int(data[0])] + [float(num) for num in data[1:]]
        data_array.append(data_float)
    for data in data_array:
        data[1] = data[1]/2
        data[2] = data[2]/2
        data[3] = data[3]/2
        data[4] = data[4]/2
    return data_array


def right_top(lines):
    data_array=[]
    for line in lines:
        data = line.strip().split(' ')
        data_float = [int(data[0])] + [float(num) for num in data[1:]]
        data_array.append(data_float)
    for data in data_array:
        data[1] = data[1]/2+0.5
        data[2] = data[2]/2
        data[3] = data[3]/2
        data[4] = data[4]/2
    return data_array



# 读取图片
images = [cv2.imread(img_path) for img_path in img_paths]

# 调整图片大小（缩小为原始尺寸的一半）
resized_images = [cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2)) for img in images]

# 创建新的空白图像
result = 255 * np.ones((resized_images[0].shape[0] * 2, resized_images[0].shape[1] * 2, 3), np.uint8)

# 将四张图片放置在合成图像中
result[:resized_images[0].shape[0], :resized_images[0].shape[1]] = resized_images[0]  # 左上
result[:resized_images[0].shape[0], resized_images[0].shape[1]:] = resized_images[1]  # 右上
result[resized_images[0].shape[0]:, :resized_images[0].shape[1]] = resized_images[2]  # 左下
result[resized_images[0].shape[0]:, resized_images[0].shape[1]:] = resized_images[3]  # 右下

# 显示合成后的图像
cv2.imshow('Merged Image', result)
cv2.imwrite('Merged Image.png', result)
cv2.waitKey(0)
cv2.destroyAllWindows()

if __name__ == '__main__':
    data0 = left_top(line0)
    data1 = right_top(line1)
    data2 = left_bottom(line2)
    data3 = right_bottom(line3)


    with open("demo.txt","w") as f:
        for row in data0:
            row_str = " ".join(str(elm) for elm in row)
            f.write(row_str+"\n")
        for row in data1:
            row_str = " ".join(str(elm) for elm in row)
            f.write(row_str+"\n")
        for row in data2:
            row_str = " ".join(str(elm) for elm in row)
            f.write(row_str+"\n")
        for row in data3:
            row_str = " ".join(str(elm) for elm in row)
            f.write(row_str+"\n")
# -* -coding:utf-8 -*-
# @Time: 2020-07-03 15:26
# @Author: ShiHua
# @file: test_pillow.py

from PIL import Image

file_path = '/Users/shihua/Desktop/founder_test/math/image_temp_cf82d932-8a5c-4fb5-a9cd-4e206a2e7bb5.jpg'

img = Image.open(file_path)
img_size = img.size

print(img_size)
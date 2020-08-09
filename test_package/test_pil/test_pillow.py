# -* -coding:utf-8 -*-
# @Time: 2020-07-03 15:26
# @Author: ShiHua
# @file: test_pillow.py

from PIL import Image
import requests
from io import StringIO, BytesIO


file_path = '/Users/shihua/Desktop/founder_test/math/image_temp_cf82d932-8a5c-4fb5-a9cd-4e206a2e7bb5.jpg'
url = 'https://xdoc-stable.oss-cn-shanghai.aliyuncs.com/open/2f4df57fc7b132c641549de2/image/tmp/0a2e593b5e6848088705.png'

content = requests.get(url).content
print(type(content))
print(type(BytesIO(content)))
img = Image.open(BytesIO(content))
img_size = img.width

print(img_size)
# -* -coding:utf-8 -*-
# @Time: 2020-06-11 16:08
# @Author: ShiHua
# @file: t.py
from bs4 import BeautifulSoup

html_doc = "<p>计算反应热最基本的方法是应用盖斯定律。</p>" \
           "<p><img alt=\"\" src=\"http://xdoc-stable.oss-cn-shanghai.aliyuncs.com/image/temp/dc852463-b2a7-45a8-85b1-2d6f1216aef0.jpg\"/></p>" \
           "<p>依据规律、经验和常识可直接判断不同反应的$$\\Delta H$$的大小。</p>" \
           "<p>（1）吸热反应的$$\\Delta H$$肯定比放热反应的大(前者大于0，后者小于0);</p>" \
           "<p>（2）$$2 m o l H _ { 2 }$$燃烧放出的热量肯定比$$1 m o l H _ { 2 }$$燃烧放出的热量多；</p>" \
           "<p>（3）等量的碳完全燃烧生成$$C O _ { 2 }$$放出的热量肯定比不完全燃烧生成$$C O$$放出的热量多；</p>" \
           "<p>（4）生成等量的水时，强酸和强碱的稀溶液反应比弱酸和强碱（或强酸和弱碱）的稀溶液反应放出的热量多；</p>"

soup = BeautifulSoup(html_doc, 'html.parser')

img_lst = []
for img in soup.find_all('img'):
    img_lst.append(img['src'])
print(img_lst)

print('---------------------------\n')

text_lst = []
for node in soup.find_all('img'):
    print(node.attrs)


h = "<span data-label='blank' data-blank-length='6'></span>"
s = soup.find_all('span')
print(f'>>>s: {s}')

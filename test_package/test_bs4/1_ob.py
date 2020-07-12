
# -* -coding:utf-8 -*-
# @Time: 2020-06-11 11:22
# @Author: ShiHua
# @file: 1_ob.py
from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc)
# Name
tag = soup.p
print(tag.name)

# Attrbutes
tag = soup.a
class_attr = tag['class']
before_attr = tag.attrs
del tag['href']
del tag['class']
del tag['id']
after_attr = tag.attrs
print(f'class_attr:{class_attr}, before_attr:{before_attr}, after_attr:{after_attr}')

# 多值属性

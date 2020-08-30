# -* -coding:utf-8 -*-
# @Time: 2020-06-12 16:34
# @Author: ShiHua
# @file: t2.py
import bs4
import re

html = "<p>计算反应热最基本的方法是应用盖斯定律。高考题中往往给出几个已知的热化学方程式，然后要求计算与之有关的目标热化学方程式的反应热，此时可应用盖斯定律进行计算。</p>" \
       "<p><img alt=\"\" src=\"http://xdoc-stable.oss-cn-shanghai.aliyuncs.com/image/temp/dc852463-b2a7-45a8-85b1-2d6f1216aef0.jpg\"/></p>" \
       "<p>依据规律、经验和常识可直接判断不同反应的$$\\Delta H$$的大小。</p>" \
       "<p>（1）吸热反应的$$\\Delta H$$肯定比放热反应的大(前者大于0，后者小于0);</p>" \
       "<p>（2）$$2 m o l H _ { 2 }$$燃烧放出的热量肯定比$$1 m o l H _ { 2 }$$燃烧放出的热量多；</p>" \
       "<p>（3）等量的碳完全燃烧生成$$C O _ { 2 }$$放出的热量肯定比不完全燃烧生成$$C O$$放出的热量多；</p>" \
       "<p>（4）生成等量的水时，强酸和强碱的稀溶液反应比弱酸和强碱（或强酸和弱碱）的稀溶液反应放出的热量多；</p>" \
       "<p><img alt=\"\" src=\"http://xdoc-stable.oss-cn-shanghai.aliyuncs.com/image/temp/dc852463-b2a7-45a8-85b1-2d6f1216aef0.jpg\"/></p>"

has_p = bool(re.search(r'<p.*?>.*?</p>', html, re.IGNORECASE))
if not has_p:
    html = f'<p>{html}</p>'

soup = bs4.BeautifulSoup(html, features='lxml')


def transform(html_nodes):
    res = []
    print(f'???? html_nodes: {html_nodes}')

    for node in html_nodes:
        if node.name == 'img':
            continue
        if isinstance(node, bs4.Tag):
            if 'class' in node.attrs:
                attr = node['class']
                res.append(f'[{node.name}]{attr}{transform(node.children)}!{attr}[!{node.name}]')
            else:
                print(f'>>>>node.name:{node.name}')
                print(f'>>>>node.children:{node.children}')
                for one in node.children:
                    print(f'>>>>>>>>>>>>>>>>>>node.children.one: {one}')
                res.append(f'[{node.name}]{transform(node.children)}[!{node.name}]')
        elif isinstance(node, bs4.NavigableString):
            res.append(str(node))
    return '\n'.join(res).replace('[p][!p]\n', '').replace('[p][!p]', '')


def transform_html():
    """
    转换html标签
    :param html_doc: html文本
    :return: 转换后的文本
    """
    html_nodes = soup.body.find_all(name='p', recursive=False)

    def handler(html_nodes):
        res = []
        for node in html_nodes:
            print(f'???? html_nodes: {html_nodes}')
            if node.name == 'img':
                continue
            if isinstance(node, bs4.Tag):
                if 'class' in node.attrs:
                    attr = node['class']
                    res.append(f'[{node.name}]{attr}{handler(node.children)}!{attr}[!{node.name}]')
                else:
                    print(f'node.name:{node.name}')
                    print(f'node.children:{node.children}')
                    for one in node.children:
                        print(f'node.children.one: {one}')
                    res.append(f'[{node.name}]{handler(node.children)}[!{node.name}]')

            elif isinstance(node, bs4.NavigableString):
                res.append(str(node))
        return ''.join(res).replace('[p][!p]', '')
    return handler(html_nodes)


print('input :', html)
# res = transform(soup.body.find_all(name='p', recursive=False))
# print('output:', res)
res1 = transform_html()
print('output:', res1)

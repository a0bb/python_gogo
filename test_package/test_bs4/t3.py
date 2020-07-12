# -* -coding:utf-8 -*-
# @Time: 2020-06-15 17:47
# @Author: ShiHua
# @file: t3.py
import bs4
import re
import json

html = "<p class='align-center'><span data-label='blank' data-blank-length='6'></span><u>计算</u>反应热<span data-label='emphasis_dot'>最</span>基本的方法是应用盖斯定律。</p>" \
           "<p>依据规律、经验和常识可直接判断不同反应的大小。</p>" \
           "<p>（1）吸热反应的肯定比放热反应的大</p>" \
           "<p>（2）燃烧放出的热量肯定比燃烧放出的热量多；</p>" \
           "<p>（3）等量的碳完全燃烧生成放出的热量肯定比不完全燃烧生成放出的热量多；</p>" \
           "<p>（4）生成等量的水时，强酸和强碱的稀溶液反应比弱酸和强碱的稀溶液反应放出的热量多；</p>"


def handle_para(nodes, base_style=None):
    """处理p"""
    paras = []
    for node in nodes:
        if not isinstance(node, bs4.Tag):
            continue
        style = {**(base_style or {}), **get_para_style(node)}
        inlines = handle_inline(node.children)
        paras.append({'style': style, 'inlines': inlines})
    return paras


def get_para_style(p):
    """转换p的样式属性"""
    style = {}
    cls = p.attrs.get('class', [])
    cls_names = ' '.join(cls)
    m = re.search(r'indent-(\d)', cls_names)
    if m:
        style['indent'] = m.group(1)
    m = re.search(r'align-(\w+)', cls_names)
    if m:
        style['align'] = m.group(1)

    return style


def handle_inline(nodes, parent_style=None):
    """处理每个节点"""
    inlines = []
    for node in nodes:
        if isinstance(node, bs4.NavigableString):
            inlines.append({'style': parent_style, 'text': str(node)})
        elif isinstance(node, bs4.Tag):
            style = {**(parent_style or {}), **get_inline_style(node)}
            inlines += handle_inline(node.children, style)
    return inlines


def get_span_style(span):
    """转换span的样式属性"""
    style = {}
    data_label = span.attrs.get('data-label', '')
    if data_label:
        style['data_label'] = span.attrs['data-label']
    data_blank_length = span.attrs.get('data-blank-length', '')
    if data_blank_length:
        style['data_blank_length'] = span.attrs['data-blank-length']

    return style


def get_inline_style(node):
    """转换节点样式属性"""
    style = {}
    if node.name == 'b':
        style['bold'] = True
    if node.name == 'i':
        style['italic'] = True
    if node.name == 'u':
        style['underline'] = True
    if node.name == 'span':
        style = get_span_style(node)
    # TODO 其他样式
    return style


soup = bs4.BeautifulSoup(html, features="lxml")

paras = handle_para(soup.body.children)

print(json.dumps(paras))

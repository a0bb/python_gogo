# -* -coding:utf-8 -*-
# @Time: 2020-06-12 11:37
# @Author: ShiHua
# @file: t1.py

import bs4
import re

html = '''
<p>test <b>bold <i>italic</i>&nbsp;</b>text</p >
<p>test1 <b>bold1 <i>italic1</i>&nbsp;</b>text1</p >
'''

has_p = bool(re.search(r'<p.*?>.*?</p >', html, re.IGNORECASE))
if not has_p:
    html = f'<p>{html}</p >'

soup = bs4.BeautifulSoup(html, features='lxml')


def transform(html_doc):
    res = ''

    def handler(html_doc, path):
        nonlocal res
        for node in html_doc:
            print(f'>>>path: {path}')
            print(f'>>>node: {node}')
            print(f'>>>>path + node: {path + [node]}')

            if isinstance(node, bs4.Tag):
                handler(node.children, path + [node])
            elif isinstance(node, bs4.NavigableString):
                if path:
                    tag_names = ''.join(n.name for n in path)
                    print(f'>>>tag_name: {tag_names}')
                    res += f'[{tag_names}]{node}[!{tag_names}]'
                else:
                    res += str(node)

    handler(html_doc, [])
    return res


res = transform(soup.body.find_all(name='p', recursive=False))
print('input :', html)
print('output:', res)

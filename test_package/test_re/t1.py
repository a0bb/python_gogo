# -* -coding:utf-8 -*-
# @Time: 2020-06-18 09:20
# @Author: ShiHua
# @file: t1.py

import re

s = 'A23G4HFD567'


def re_match():
    """
    re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
    """
    match_s = re.match(r'(?P<value>\d+)', s)
    print(f're match: {match_s}')


def re_search():
    search_s = re.search(r'(?P<value>\d+)', s)
    print(f're search: {search_s.group(1)}')


def re_sub_01():
    phone = "2004-959-559 # 这是一个国外电话号码"
    # 删除字符串中的 Python注释
    num = re.sub(r'#.*$', '', phone)
    print(f'电话号码: {num}')
    # 删除非数字(-)的字符串
    num = re.sub(r'\D', '', phone)
    print(f'电话号码: {num}')


def re_sub_02():
    def double(matched):
        value = int(matched.group('value'))
        return str(value * 2)

    new_s = re.sub(r'(?P<value>\d+)', double, s)
    print(new_s)


def re_compile():
    pattern = re.compile(r'\d+')
    m = pattern.match('one12twothree34four')
    print(m)

    m = pattern.match('one12twothree34four', 3, 10)
    print(f'_sre.SRE_Match object: {m}')
    print(f'm.group(0): {m.group(0)}')

    print('-' * 50)

    pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)
    m = pattern.match('Hello World Wide Web')
    print(f'_sre.SRE_Match object: {m}')
    print(f'm.group(0): {m.group(0)}')
    print(f'm.group(1): {m.group(1)}')
    print(f'm.group(2): {m.group(2)}')
    print(f'm.group(3): {m.group(3)}')


def re_findall():
    pattern = re.compile(r'\d+')  # 查找数字
    result1 = pattern.findall('runoob 123 google 456')
    result2 = pattern.findall('run88oob123google456', 0, 10)

    print(result1)
    print(result2)


def re_finditer():
    it = re.finditer(r"\d+", "12a32bc43jf3")
    for match in it:
        print(match.group())


def re_split():
    pass


if __name__ == '__main__':
    phone = "2004-959-559 # 这是一个国外电话号码"
    num = re.sub(r'#.*外', '', phone)

    print(num)

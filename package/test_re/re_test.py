# -* -coding:utf-8 -*-
# @Time: 2020-06-21 17:10
# @Author: ShiHua
# @file: re_test.py
import re

test = ''
s = "化学###错误占位->id:110###反应;化学###错误占位->id:111###反应;" \
    "化学###错误占位->id:112###反应;化学###错误占位->id:113###反应"

i = 0
res = re.findall(r'(###错误占位->id:.*?###)', s)
print(res)


def repl(_):
    global i
    _id = res[i]
    i += 1
    _id = f'update{_id}'
    print(_id)
    return _id


p = re.sub(r'(###错误占位->id:.*?###)', repl, s)
print(p)


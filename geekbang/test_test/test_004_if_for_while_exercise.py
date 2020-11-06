# -*- coding:utf-8 -*-
#
# @author: shihua
# 
# @time: 2020-02-02 13:33

# 最后给你留一个思考题。
# 给定下面两个列表 attributes 和 values，要求针对 values 中每一组子列表 value，输出其和 attributes 中的键对应后的字典，
# 最后返回字典组成的列表。
# expected output:
# [{'name': 'jason', 'dob': '2000-01-01', 'gender': 'male'},
#  {'name': 'mike', 'dob': '1999-01-01', 'gender': 'male'},
#  {'name': 'nancy', 'dob': '2001-02-01', 'gender': 'female'}]
# 你能分别用一行和多行条件循环语句，来实现这个功能吗？

attributes = ['name', 'dob', 'gender']
values = [
    ['jason', '2000-01-01', 'male'],
    ['mike', '1999-01-01', 'male'],
    ['nancy', '2001-02-01', 'female']
]
lst = []
for v in values:
    dct = {}
    for index, item in enumerate(attributes):
        dct[item] = v[index]
    lst.append(dct)
print(lst)


lst = [dict(zip(attributes, v)) for v in values]
print(lst)


"""
map(function, iterable, ...)
zip([iterable, ...])
"""
a = [1, 2, 3]
b = [4, 5, 6]
c = [4, 5, 6, 7, 8]
z = zip(a, b, c)
print(z)
print(list(z))
z = zip(a, b)
print(dict(z))


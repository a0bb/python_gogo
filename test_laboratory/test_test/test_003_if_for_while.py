# -*- coding:utf-8 -*-
#
# @author: shihua
# 
# @time: 2020-02-02 11:31

# l = [-1, -2, -3, -4, -5, -6, -7]
# #
# # # index 索引   item 索引对应的值
# # for index, item in enumerate(l):
# #     print(index, item)


# # 给定两个字典，分别是产品名称到价格的映射，和产品名称到颜色列表的映射。我们要找出价格小于 1000，并且颜色不是红色的所有产品名称和颜色的组合。
# name_price = {
#     'apple': 20,
#     'pen': 2000,
#     'banana': 55
# }
# name_color = {
#     'apple': ['red'],
#     'pen': ['white'],
#     'banana': ['yellow', 'red'],
#     'water': ['white']
# }
#
# for name, price in name_price.items():
#     if price > 1000:
#         continue
#     if name not in name_color:
#         print(f'name: {name}, color: None')
#     for color in name_color[name]:
#         if color == 'red':
#             continue
#         print(f'name: {name}, color: {color}')


# # y = 2*|x| + 5
# x = [1, 2, 3]
# y = [value if value>0 else -value for value in x]


# 将文件中逐行读取的一个完整语句，按逗号分割单词，去掉首位的空字符，并过滤掉长度小于等于 5 的单词，最后返回由单词组成的列表。
# text = ' Today, is, Sunday'
# text_lst = [t.strip() for t in text.split(',') if len(t.strip()) > 5]
# print(text_lst)


# 比如，给定两个列表 x、y，要求返回 x、y 中所有元素对组成的元祖，相等情况除外。
x = [1, 2, 3]
y = [4, 5, 6]
z = [(xx, yy) for xx in x for yy in y if xx != yy]
print(z)
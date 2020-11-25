# -*- coding:utf-8 -*-
#
# @author: shihua
# 
# @time: 2020-02-02 22:26

#
# class MyInputError(Exception):
#     """Exception raised when there're errors in input"""
#     def __init__(self, value):  # 自定义异常类型的初始化
#         self.value = value
#
#     def __str__(self):  # 自定义异常类型的string表达形式
#         return ("{} is invalid input".format(repr(self.value)))
#
#
# try:
#     raise MyInputError(1)  # 抛出MyInputError这个异常
# except MyInputError as err:
#     print('error: {}'.format(err))


import ujson
with open('../../geekbang/mock_data.json', 'r', encoding='utf-8') as fp:
    mock_data = ujson.load(fp)
    print(mock_data['bind_info'])
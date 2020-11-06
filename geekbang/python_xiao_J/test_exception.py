# -*- coding:utf-8 -*-
"""
@author: SHIHUA
@file: test_exception.py
@time: 2019/11/24 10:51
"""
import traceback

# try:
#     s = input("please enter two numbers separated by comma:")
#     print(type(s), s)
#     num1 = int(s.split(',')[0].strip())
#     num2 = int(s.split(',')[1].strip())
#     print(num1, num2)
# except ValueError as err:
#     print('Value Error: {}'.format(err))
# # except IndexError as err:
# #     print('Index Error: {}'.format(err))
# except Exception as e:
#     print('Other Error: {}'.format(e))
# except:
#     print('Other Error: \n{}'.format(traceback.format_exc()))
# print('continue......')


# class MyInputError(Exception):
#     def __init__(self, input):
#         self.input = input
#
#     def __str__(self):
#         return '{} is invalid input'.format(repr(self.input))
#
#
# try:
#     raise MyInputError(1)
# except MyInputError as err:
#     print('error: {}'.format(err))


# def factorial(input):
#     if not isinstance(input, int):
#         raise Exception('input must be an integer.')
#     if input < 0:
#         raise Exception('input must be greater or equal to 0')
#     ...
#
#     def inner_factorial(input):
#         if input <= 1:
#             return 1
#         return input * inner_factorial(input - 1)
#
#     return inner_factorial(input)
#
#
# print(factorial(5))
#
#
# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n-1)
#
# print(fact(10))





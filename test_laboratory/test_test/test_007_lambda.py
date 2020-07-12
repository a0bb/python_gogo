# -*- coding:utf-8 -*-
#
# @author: shihua
# 
# @time: 2020-03-14 19:32

l = [1, 2, 3, 4, 5]
new_lst = map(lambda x: x ** 2, l)
print(new_lst)
print(list(new_lst))
print('-' * 50)

new_lst = filter(lambda x: x % 2, l)
print(new_lst)
print(list(new_lst))
print('-' * 50)

f = lambda x, y: x * y
print(f(1, 2))
print('-' * 50)

from functools import reduce
product = reduce(lambda x, y: x * y, l)
print(product)
print('-' * 50)


# 第一问：如果让你对一个字典，根据值进行由高到底的排序，该怎么做呢？以下面这段代码为例，你可以思考一下。
d = {'mike': 10, 'lucy': 2, 'ben': 30}
s = sorted(d.items(), key=lambda x: x[1], reverse=True)
print(s)


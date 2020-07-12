# -*- coding:utf-8 -*-
#
# @author: shihua
# 
# @time: 2020-03-15 21:22

l1 = [1, 2, 3]
l2 = [1, 2, 3]
l3 = l2

print(id(l1))
print(id(l2))
print(id(l3))


def func(x):
    x['a'] = 10
    x['b'] = 20

d = {'a': 1, 'b': 2}
func(d)
print(d)
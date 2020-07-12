# -*- coding:utf-8 -*-
#
# @author: shihua
# 
# @time: 2020-03-15 20:23

# x = 1
# def func():
#     x += 1
# func()


MIN_VALUE = 1
MAX_VALUE = 10

def validation_check():
    global MIN_VALUE
    MIN_VALUE += 1
    print(MIN_VALUE)

validation_check()
print(MIN_VALUE)

print('-' * 50)
x = [1]
def func():
    x.append(2)
func()
print(x)
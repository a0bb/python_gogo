# -*- coding:utf-8 -*-
#
# @author: shihua
# 
# @time: 2020-04-01 23:17


def mydecorate(func):
    def wrapper():
        print('in wrapper')
        func()
    return wrapper


@mydecorate
def green():
    print('in green')

green()
print('-' * 100)

# 带有参数的装饰器
def mydecorate01(func):
    def wrapper(*args, **kwargs):
        print('in wrapper')
        func(*args, **kwargs)
    return wrapper

@mydecorate01
def green01(name, color):
    print(f'{name} is {color}')

green01('xiaoeyu', 'green')
print('-' * 100)


# 带有自定义参数的装饰器
def repeat(num):
    def decoretor(func):
        def wrapper(*args, **kwargs):
            for i in range(num):
                print('in wrapper')
                func(*args, **kwargs)
        return wrapper
    return decoretor

@repeat(5)
def green(message):
    print(message)

green('in green~')
print('-' * 100)

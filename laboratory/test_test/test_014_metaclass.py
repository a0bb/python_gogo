# -*- coding:utf-8 -*-
#
# @author: shihua
# 
# @time: 2020-04-02 23:06

lst = [1, 3, 4]
isinstance(lst, list)


def is_iterable(param):
    try:
        iter(param)
        return True
    except TypeError:
        return False


def show_memory_info(hint):
    import os, psutil
    pid = os.getpid()
    p = psutil.Process(pid)
    info = p.memory_full_info()
    memory = info.uss / 1024. / 1024
    print('{} memory used: {} MB'.format(hint, memory))


def test_iterator():
    show_memory_info('initing iterator')
    list_1 = [i for i in range(100000000)]
    show_memory_info('after iterator initiated')
    print(sum(list_1))
    show_memory_info('after sum called')

def test_generator():
    show_memory_info('initing generator')
    list_2 = (i for i in range(100000000))
    show_memory_info('after generator initiated')
    print(sum(list_2))
    show_memory_info('after sum called')


test_iterator()

test_generator()
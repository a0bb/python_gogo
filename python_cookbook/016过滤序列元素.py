
my_list = [1, -1, 2, -3, 3, -10, 5, -7]

case1 = [item for item in my_list if item > 0]
print(f'case1: {case1}')

case2 = [item for item in my_list if item < 0]
print(f'case2: {case2}')

# 如果my_list过大则会生成一个很大的结果集，考虑到内存的问题，可以使用生成器表达式
case3 = (item for item in my_list if item > 0)
print(f'case3: {case3}')

for item in case3:
    print(item)
print('*' * 100)

"""
https://docs.python.org/3.6/library/functions.html#filter
filter(function, iterable)
iterable可以是序列，支持迭代的容器或迭代器；function逐个判断iterable内的元素，如果返回True，则作为filter的返回数据
"""
values = ['str', 1, None, False, True, 2, 3, -1, 0]


def is_int(val):
    if not isinstance(val, bool) and isinstance(val, int):
        return True
    else:
        return False


case4 = list(filter(is_int, values))
print(f'case4: {case4}')

# itertools.filterfalse()为filter()的互补函数，该函数返回function返回为false的iterable元素。
import itertools
case5 = list(itertools.filterfalse(is_int, values))
print(f'case5: {case5}')

# 如果function为None，则删除所有false的iterable元素
case6 = list(filter(None, values))
print(f'case6: {case6}')


# 列表推导和生成器表达式可以在过滤时转换数据
my_list = [-3, -2, -1, 0, 1, 2, 3]
import math
case7 = [math.sqrt(item) for item in my_list if item > 0]
print(f'case7: {case7}')


# 列表推导和生成器表达式 + 三元表达式
my_list = [-3, -2, -1, 0, 1, 2, 3]
case8 = [n if n > 0 else None for n in my_list]
print(f'case8: {case8}')


# 另外一个值得关注的过滤工具就是itertools.compress()，它以一个iterable对象和一个相对应的Boolean选择器序列作为输入参数。
# 然后输出iterable对象中对应选择器为True的元素。 当你需要用另外一个相关联的序列来过滤某个序列的时候，这个函数是非常有用的。
# 比如，假如现在你有下面两列数据：
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]

from itertools import compress
more5 = [n > 5 for n in counts]
case9 = list(compress(addresses, more5))
print(f'case9: {case9}')

# 这里的关键点在于先创建一个Boolean序列，指示哪些元素符合条件。然后compress()函数根据这个序列去选择输出对应位置为True的元素。
# 和filter()函数类似，compress()也是返回的一个迭代器。因此，如果你需要得到一个列表， 那么你需要使用list()来将结果转换为列表类型。

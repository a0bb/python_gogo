rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

# 注意事项：先排序再分组
# 原因： groupby() 函数扫描整个序列并且查找连续相同值（或者根据指定 key 函数返回值相同）的元素序列。

from operator import itemgetter
from itertools import groupby


new_rows = sorted(rows, key=itemgetter('date'))
group_rows = groupby(new_rows, key=itemgetter('date'))
# 从下面可以看出，返回的是一个迭代器对象
print(f'>>>type: {type(group_rows)}')
print(f'>>>group_rows: {group_rows}')
# 转成列表看下，列表由固定格式的元组组成
# 元组中包含分组的key及其这个组包含的元素（组内元素是一个迭代器对象）
print(f'>>>list: {list(group_rows)}')


# 按照分组来输出
print('*' * 100)
# 这里为什么不直接使用group_rows，而是又重写了一次groupby(new_rows, key=itemgetter('date'))
# 因为，迭代器经过list(group_rows)就被消耗掉了
for date, items in groupby(new_rows, key=itemgetter('date')):
    print(date)
    for item in items:
        print(f'  {item}')


def group_01(rows, key):
    new_obj = sorted(rows, key=itemgetter(key))
    group_dict = {}
    for group_v, items in groupby(new_obj, key=itemgetter(key)):
        group_dict[group_v] = list(items)
    return group_dict

# 0006 多值字典
from collections import defaultdict
def group_02(rows, key):
    rows_by_key = defaultdict(list)
    for row in rows:
        rows_by_key[row[key]] = row
    return rows_by_key


# 使用groupby的方式，需要先排序，再分组，过程中都是对迭代器的操作，所以对内存占用量（空间）要小一些
# 使用defaultdict的方式，不需要排序，时间上相对更快一些，如果对内存占用不太关心，defaultdict是个不错的选择。
# 按需选择。


if __name__ == '__main__':
    print(group_02(rows, 'date'))

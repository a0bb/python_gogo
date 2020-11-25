# 首先介绍下sorted()方法
# sorted(iterable, key=None, reverse=False)
# iterable 可迭代对象
# key 接收一个callable()对象作为排序的依据
# reverse 排序规则  True降序  False升序 （默认False）


from operator import itemgetter

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

case1 = sorted(rows, key=lambda x: x['fname'])
print(f'case1 -> {case1}')

# 注意：str不能和int作比较，使用items()转换后做比较的时候切忌检查好数据类型
row = {'width_1': 1001, 'width_2': 1000, 'width_3': 1006}
case2 = sorted(row.items(), key=lambda x: x[1])
print(f'case2 -> {case2}')
case3 = sorted(row.items(), key=itemgetter(1))
print(f'case3 -> {case3}')

# 使用itemgetter() 比lambda要快一些

rows_by_fname = sorted(rows, key=itemgetter('fname'))
print(f'rows_by_fname: {rows_by_fname}')
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(f'rows_by_uid: {rows_by_uid}')


# 同时支持对多个key进行排序
# 比如需求是，同时对姓和名进行排序
rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print(f'rows_by_lfname: {rows_by_lfname}')


case4 = min(rows, key=itemgetter('uid'))
case5 = max(rows, key=itemgetter('uid'))
print(f'case4 -> {case4}')
print(f'case5 -> {case5}')


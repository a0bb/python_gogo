# 首先介绍下sorted()方法

from operator import itemgetter



rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

r1 = sorted(rows, key=lambda x: x['fname'])
print(r1)

rows_1 = {'fname': 'Brian', 'lname': 'Jones', 'uid': "1003"}
# 注意：str不能和int作比较，使用items()转换后做比较的时候切忌检查好数据类型
r2 = sorted(rows_1.items(), key=lambda x: x[1])
print(r2)
r3 = sorted(rows_1.items(), key=itemgetter(1))
print(r3)

# 使用itemgetter() 比lambda要快一些

rows_by_fname = sorted(rows, key=itemgetter('fname'))
print(f'rows_by_fname: {rows_by_fname}')
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(f'rows_by_uid: {rows_by_uid}')


# 同时支持对多个key进行排序
# 比如需求是，同时对姓和名进行排序
rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print(f'rows_by_lfname: {rows_by_lfname}')


min(rows, key=itemgetter('uid'))
max(rows, key=itemgetter('uid'))

nums = [1, 2, 3, 4, 5]
case1 = sum(i ^ 2 for i in nums)
print(case1)


import os
files = os.listdir('dirname')

if any(item.endswith('.py') for item in files):
    print('has py file')
else:
    print('no py file')


s = ('a', 1, 3)
print(','.join(str(i) for i in s))


portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 65}
]
print(min(item['shares'] for item in portfolio))


# 上面提到了any的用法，由此想到了all，下面一起看一下
print(any([True, False, True]))

print(any([False, False, False]))

print(all([True, False, True]))

print(all([True, True, True]))

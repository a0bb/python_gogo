""" 多值字典的写入 """


from collections import defaultdict


d = defaultdict(list)
d['number'].append(110)
d['number'].append(120)
print(f'd: {d}')

s = defaultdict(set)
s['number'].add(110)
s['number'].add(110)
print(f's: {s}')

# setdefault，不自然且每次调用都会初始化一个新的实例（空列表）
d = {}
d.setdefault('number', []).append(110)
d.setdefault('number', []).append(120)
print(f'setdefault d: {d}')

# 对多值字典的第一个值做初始化
# 低效的写法
d = {}
dct = {'name': 'ed', 'number': ['110', '120']}
for k, v in dct:
    if k not in d:
        d[k] = []
    d[k].append(v)

# 使用defaultdict
d = defaultdict(list)
for k, v in dct:
    d[k].append(v)

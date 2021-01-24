from collections import ChainMap


a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

c1 = ChainMap(a, b)
print(c1['x'], c1['y'], c1['z'])

c2 = ChainMap(b, a)
print(c2['x'], c2['y'], c2['z'])

print(len(c1))

print(list(c1.keys()))

print(list(c1.values()))


# 更新或者删除总是影响的是第一个字典
print(f'origin_a:{a}  origin_b:{b}')
c1['z'] = 10
c1['w'] = 40
del c1['x']
print(f'a:{a}  b:{b}')

# del c1['y']

print('*' * 100)
# 处理作用范围
values = ChainMap()

values['x'] = 1
print(values)

values = values.new_child()
print(values)
values['x'] = 10
print(values)

values = values.new_child()
values['x'] = 100
print(values)


print(values['x'])

values = values.parents
print(values['x'])

values = values.parents
print(values['x'])


print('*' * 100)
# 和update有什么区别？
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
a.update(b)
print(a['y'])
b['y'] = 20
print(a['y'])


a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merge = ChainMap(a, b)
print(merge['y'])
b['y'] = 20
print(merge['y'])

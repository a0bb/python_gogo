
s = '0123456789'

s1 = s[1:3]
s2 = s[3:]
s3 = s[:3]
s4 = s[1:8:2]

slice_1 = slice(1, 3)
slice_2 = slice(3, None)
slice_3 = slice(3)
slice_4 = slice(1, 8, 2)

equal_s1 = s[slice_1]
equal_s2 = s[slice_2]
equal_s3 = s[slice_3]
equal_s4 = s[slice_4]

print(f'{s1} - {s2} - {s3} - {s4}')

print(f'{equal_s1} - {equal_s2} - {equal_s3} - {equal_s4}')

print('-' * 100)
# 所有可以使用切片的地方，都可以使用切片对象
items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
print(f'items[2:4] -> {items[2:4]}')
print(f'items[a] -> {items[a]}')

items[a] = [10, 11]
print(f'items -> {items}')

del items[a]
print(f'items -> {items}')

print('-' * 100)
# more
a = slice(1, 30, 2)
print(f'a.start -> {a.start}')
print(f'a.stop -> {a.stop}')
print(f'a.step -> {a.step}')

# 使用indices将它映射到一个已知大小的序列上。 这个方法返回一个三元组 (start, stop, step) ，所有的值都会被缩小，直到适合这个已知序列的边界为止。
# 用法如下
s = 'i love china.'
a = slice(1, 30, 2)
print(f'a.indices -> {a.indices(len(s))}')
a = slice(1, 30)
print(f'a.indices -> {a.indices(len(s))}')


prices = [2.1, 4.3, 5.4, 2.6, 4.7]
print(prices[slice(2, 4)])

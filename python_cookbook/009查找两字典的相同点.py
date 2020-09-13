""" 查找两字典的相同点 """
# 指的是字典的相同的值或者相同的键

a = {
    'x': 1,
    'y': 2,
    'z': 3
}
b = {
    'x': 11,
    'y': 2,
    'w': 10
}
c = {
    'x': 100,
    'b': 20,
    'w': 40
}

print(a.keys())
print(a.values())
print(a.items())

# 字典的<keys()>和<items()>支持集合操作（并、交、差） 所以对字典的<keys()>和<items()>进行集合操作的时候不需要转为set。
print(a.keys() & b.keys() & c.keys())
print(a.keys() | b.keys())
print(a.keys() - b.keys())

print(a.items() & b.items())
print(a.items() | b.items())
print(a.items() - b.items())

# 字典的<values()>不支持集合操作，因为不能保证<values()>的值互不相同。
# a.values() & b.values()，


# 这些操作也可以用于修改或者过滤字典元素。 比如，假如你想以现有字典构造一个排除几个指定键的新字典。 下面利用字典推导来实现这样的需求：

# Make a new dictionary with certain keys removed
c = {key: a[key] for key in a.keys() - {'z', 'w'}}
# c is {'x': 1, 'y': 2}

print(c)




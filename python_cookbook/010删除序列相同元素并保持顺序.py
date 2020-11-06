
""" 删除序列相同元素并保持顺序 """

"""
https://www.lfhacks.com/tech/immutable-hashable-in-python
哈希表是在一个关键字和一个较大的数据之间建立映射的表，能使对一个数据序列的访问过程更加迅速有效。用作查询的关键字必须唯一且固定不变，于是只有immutable的对象才可以作为键值，“可以作为键值”这种属性，叫hashable.
"""


def hashable_dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item  # 把这函数变成一个generator
            seen.add(item)  # 把有效元素加入集合


def unhashable_dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key[item]
        if val not in seen:
            yield item
            seen.add(val)


# yield https://blog.csdn.net/mieleizhi0522/article/details/82142856


a = (i for i in range(0, 10))
print(a)
print(type(a))


def ff(a):
    for i in a:
        yield i
        print(i)
ff(a)


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item  # 把这函数变成一个generator
            seen.add(item)  # 把有效元素加入集合


def dedupe_1(items):
    seen = set()
    for item in items:
        if item not in seen:
            seen.add(item)
    return seen


a = [1, 3, 4, 5, 4, 8, 9, 1]
print(dedupe(a), '->', list(dedupe(a)))
print(dedupe_1(a))

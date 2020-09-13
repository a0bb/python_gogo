""" 字典的运算  """

# 核心： ......

# 首先，一起来了解下一个内置函数的用法 （zip）
# zip用来把多个对象中对应的元素打包成为一个个元组；input可迭代对象，output迭代器
a = [1, 2, 3]
b = ['a', 'c', 'd', 'e']
c = ['b', 'f', 'd', 'h', 'g']

case1 = zip(a, b)
print(f'List zip function case1: {list(case1)}')

case2 = zip(b, c)
print(f'List zip function case2: {list(case2)}')

case3 = zip(a, b, c)
print(f'List zip function case3: {list(case3)}')

# zip()返回的迭代器只能访问一次，第二次访问会ValueError
case4 = zip(a, b, c)
print(min(case4))
# print(min(case4))  # ValueError: min() arg is an empty sequence

# 由以上case可以看出，没有配对的对象不会被打包处理


# 说过zip()就得讲一下map()这个函数，毕竟我有很长一段时间因为这两个函数长的太像而傻傻分不清
# map(function, iterable, ...)是根据指定的函数对序列做映射；
# 第一个参数为函数，第二个参数为一个或者多个序列
# 示例
def square(x):
    return x ** 2


case1 = map(square, [1, 2, 3, 4, 5])
print(case1)
print(list(case1))

# 使用lambda
case2 = map(lambda x: x ** 2, [1, 2, 3, 4, 5])
print(case2)
print(list(case2))

# 字典的运算
# 字典运算的核心是把字典转为合适的元组，然后对元组进行各种操作
# PS: 元组的比较规则，当第一个值相同时，会去比较第二个值；所以当价格相同的时候，回去根据key做比较。
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# 找出最大的价格并需要知道对应的key
max_price = max(zip(prices.values(), prices.keys()))
print(f'max_prices: {max_price}')
# 找出最小的价格并需要知道对应的key
min_price = min(zip(prices.values(), prices.keys()))
print(f'min_prices: {min_price}')
# 对价格进行排序
sort_price = sorted(zip(prices.values(), prices.keys()))
print(f'sort_price: {sort_price}')

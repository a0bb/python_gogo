
"""序列分解为单独的变量"""

case1 = [1, '2']
a, b = case1
print(f'case1 res -> {a}; {b}')

case2 = '123'
a, b, c = case2
print(f'case2 res -> {a}; {b}; {c}')

case3 = (1, '2')
a, b = case3
print(f'case3 res -> {a}; {b}')

case4 = {1, '2'}
a, b = case4
print(f'case4 res -> {a}; {b}')

case5 = {'key1': 'value1', 'key2': 'value2'}
a, b = case5
print(f'case5 res -> {a}; {b}')

case6 = ['a', 'b', ('t1', 't2'), ['l1', 'l2'], {'k1': 'v1', 'k2': 'v2'}]
a, b, t, l, d = case6
print(f'case6_01 res -> {a}; {b}; {t}; {l}; {d}')

a, b, (t1, t2), (l1, l2), (k1, k2) = case6
print(f'case6_02 res -> {a}; {b}; {t1}; {t2}; {l1}; {l2}; {k1}; {k2}')

# _ 表示为占位
case7 = ['a', 'b', 'c', 'd', 'e']
_, _, c, _, _ = case7
print(f'case7 res -> {c}')

# iterable 也可以这样来取值
l1, l2 = ['a', 'b'], ['c', 'd']
case8 = zip(l1, l2)
a, b = case8
print(f'case8 res {type(case8)} -> {a}; {b}')


"""序列分解为单独的变量"""

case1 = [1, '2']
a, b = case1
print(f'case1 result -> {a}; {b}')

case2 = '123'
a, b, c = case2
print(f'case2 result -> {a}; {b}; {c}')

case3 = (1, '2')
a, b = case3
print(f'case3 result -> {a}; {b}')

case4 = {1, '2'}
a, b = case4
print(f'case4 result -> {a}; {b}')

case5 = {'key1': 'value1', 'key2': 'value2'}
a, b = case5
print(f'case5 result -> {a}; {b}')

case6 = ['a', 'b', ('t1', 't2'), ['l1', 'l2'], {'k1': 'v1', 'k2': 'v2'}]
a, b, t, l, d = case6
print(f'case6_01 result -> {a}; {b}; {t}; {l}; {d}')

a, b, (t1, t2), (l1, l2), (k1, k2) = case6
print(f'case6_02 result -> {a}; {b}; {t1}; {t2}; {l1}; {l2}; {k1}; {k2}')

d = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7
}

case1 = {k: v for k, v in d.items() if v > 4}
print(f'case1: {case1}')

nodes = [
    {'node_id': "e3rdf", 'number': '1001'},
    {'node_id': "f5g44", 'number': '1002'},
    {'node_id': "hbj7h", 'number': '1003'},
    {'node_id': "jky7g", 'number': '1004'}
]

case2 = {item['node_id']: item for item in nodes}
print(f'case2: {case2}')

case3 = dict((item['node_id'], item) for item in nodes)
print(f'case3: {case3}')

print('*' * 100)

# dict
# class dict(**kwarg)
# class dict(mapping, **kwarg)
# class dict(iterable, **kwarg)

case1 = dict(a='one', b='two', c='three')
print(f'case1: {case1}')

case2 = dict([('a', 'one'), ('b', 'two'), ('c', 'three')])
print(f'case2: {case2}')

# [('a', 'one'), ('b', 'two'), ('c', 'three')]可以使用另一种input的形式zip(['a', 'b', 'c'], ['one', 'two', 'three'])
# zip()  008节
case3 = dict(zip(['a', 'b', 'c'], ['one', 'two', 'three']))
print(f'case3: {case3}')

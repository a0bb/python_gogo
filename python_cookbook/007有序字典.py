""" 有序字典 OrderDict """

# PS: py3.6之后，字典都为有序，可以无视这篇文章

from collections import OrderedDict
import json

# 按照元素初始添加的顺序进行排序
# 从下面可以看出，OrderDict定义的字典和普通字典用法一样
d = OrderedDict()
d['name'] = 'DaMing'
d['age'] = 20
d['number'] = 100
d['mobil'] = '10233933333'
print(f'init dict: {d}')

d.pop('number')
print(f'after pop dict:{d}')

d.update({'tag': ['student', 'man']})
print(f'after update dict: {d}')

print(f'dumps dict: {json.dumps(d)}')

# 注意
# OrderDict因为内容是一个双向链表，所以大小是普通字典的两倍多；在使用前，一定要做好需求分析。




from collections import namedtuple


Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub)
print(sub.addr)
print(sub.joined)

print('*' * 100)

print(len(sub))
addr, joined = sub
print(addr, joined)

print('*' * 100)


# 三种实例化的方法（这里叫实例化不知道是否合适）
User = namedtuple('User', ['name', 'age', 'weight'])
# 最原生的创建
cat = User('cat', '15', '50kg')
# 解包创建
user01 = ['daming', '12', '70kg']
daming = User(*user01)
# 使用_make创建
xiaohong = User._make(['xiaohong', '12', '40kg'])

print(cat.name, cat.age, cat.weight)
print(daming.name, daming.age, daming.weight)
print(xiaohong.name, xiaohong.age, xiaohong.weight)

# 替换数据
daming = daming._replace(weight='90kg')
print(daming)

# 转化为字典
daming = daming._asdict()
print(daming)
print(dict(daming))

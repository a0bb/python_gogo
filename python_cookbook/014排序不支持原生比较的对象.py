

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


u = User(1001)
print(type(u))
print(u)

# 理解 attrgetter  itemgetter
# 顾名思义，item意为一项、条，也就是对可迭代对象的每一条作比较；attr意为属性，也就是把某个对象的属性做比较

from operator import attrgetter


users = [User(1001), User(1002), User(1003), User(988)]
case1 = sorted(users, key=attrgetter('user_id'))
print(f'case1: {case1}')


case2 = sorted(users, key=lambda x: x.user_id)
print(f'case2: {case2}')


case3 = min(users, key=attrgetter('user_id'))
print(f'case3: {case3}')

case4 = max(users, key=attrgetter('user_id'))
print(f'case4: {case4}')

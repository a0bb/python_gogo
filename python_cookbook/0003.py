
""" 保存最后N个元素 """

from collections import deque

# explanation：deque 可以创建一个固定长度的队列。有新的数据插入且队列已经满时，自动删除最老的一条数据

# 用法
# 声明一个长度等于3的队列
# deque也可以不声明长度 q = deque()
q = deque(maxlen=3)
# 在队列中后面追加数据
q.append('a')
q.append('b')
q.append('c')
q.append('d')
print(f'01:{q}')
# 在队列前面添加数据
q.appendleft(-1)
print(f'02:{q}')
# 删除队列末尾的数据，返回值为被删除的数据
pop_res = q.pop()
print(f'pop_res: {pop_res}')
print(f'03:{q}')
# 删除队列前面的数据，返回值为被删除的数据
popleft_res = q.popleft()
print(f'popleft_res: {popleft_res}')
print(f'04:{q}')
# 从队列两端添加或者弹出的时间复杂度都是O(1),

print('-' * 60)


# example：从列表内查找某个数据，保留最新的5条
def search(lines, data, history=5):
    previous_lst = deque(maxlen=history)
    for line in lines:
        if data in line:
            yield line, previous_lst
            previous_lst.append(line)


if __name__ == '__main__':
    lst = ['z1', 'z2', 'z3', 'z4', 'z5', 'x1', 'z6', 'x2']
    for l in search(lst, 'z'):
        print(l)

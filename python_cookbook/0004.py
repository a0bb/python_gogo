""" 找到最大或者最小的N个元素 """

import heapq
from typing import List, Dict

numbers = [1, 2, 4, 6, -4, -3, -9, 9, 2, 8]
large_nums = heapq.nlargest(3, numbers)
small_nums = heapq.nsmallest(3, numbers)

print(f'large nums: {large_nums}')
print(f'small nums: {small_nums}')

# nlargest和nsmallest可以处理更加复杂的数据结构
dict_in_list = [
    {'name': 'ws', 'age': 23},
    {'name': 'wfm', 'age': 31},
    {'name': 'scl', 'age': 28}
]
young = heapq.nlargest(2, dict_in_list, key=lambda s: s['age'])
elderly = heapq.nsmallest(2, dict_in_list, key=lambda s: s['age'])

print(f'young: {young}')
print(f'elderly: {elderly}')


heap = list(numbers)
# list -> heap(堆)
heapq.heapify(heap)
print(f'heap: {heap}')

# 堆的重要特性是heap[0]总是最小的元素
# heapq.heappop()会将第一个元素（最小的）弹出，然后以第二小元素取而代之
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print('-' * 50)


# 找大最大的N个元素
def search(lst: List, n: int):
    if n == 1:
        return max(lst)
    elif n > (len(lst) * 0.9):
        return sorted(lst)[:n]
    else:
        return heapq.nlargest(n, lst)


if __name__ == '__main__':
    lst = [1, 3, 6, 8, 4, 5, 1]
    print(search(lst, 7))

import heapq

"""
heapq.heapify(x)
    将list x 转换成堆，原地，线性时间内
"""
heap = [1, 3, 5, 9, 3, 5, 3, 7, 2]
heapq.heapify(heap)
print(f'heap: {heap}')

"""
heapq.heappush(heap, item)
    将item的值加入到heap中，保持堆的不变性
"""
heapq.heappush(heap, 100)
print(f'after heappush: {heap}')

"""
heap.heappop(heap)
    弹出并返回heap中最小的元素，保持堆的不变性；如果堆为空，抛出 IndexError 。使用 heap[0] ，可以只访问最小的元素而不弹出它。
"""
min_num = heapq.heappop(heap)
print(f'after heappop: {heap}')
print(f'return heappop: {min_num}')

"""
heapq.heappushpop(heap, item)
    将 item 放入堆中，然后弹出并返回 heap 的最小元素。该组合操作比先调用 heappush() 再调用 heappop() 运行起来更有效率
"""
min_num = heapq.heappushpop(heap, 200)
print(f'after heappushpop: {heap}')
print(f'return heappushpop: {min_num}')

"""
heapq.heapreplace(heap, item)
    弹出并返回 heap 中最小的一项，同时推入新的 item。 堆的大小不变。 如果堆为空则引发 IndexError。
    这个单步骤操作比 heappop() 加 heappush() 更高效，并且在使用固定大小的堆时更为适宜。 pop/push 组合总是会从堆中返回一个元素并将其替换为 item。
    返回的值可能会比添加的 item 更大。 如果不希望如此，可考虑改用 heappushpop()。 它的 push/pop 组合会返回两个值中较小的一个，将较大的值留在堆中。
"""
min_num = heapq.heapreplace(heap, 300)
print(f'after heapreplace: {heap}')
print(f'return heapreplace: {min_num}')


# 实现一个优先队列
class PriorityQueue:

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


# 从下面例子可以看出，如果堆里面的对象是一个sequence类型的对象，则以index=0的元素为最小值的判断依据
# 详见heappop源码
heappop_test = [(-1, 'a'), (-5, 'v'), (-9, 'g')]
heapq.heapify(heappop_test)
min_tuple = heapq.heappop(heappop_test)
print(min_tuple)



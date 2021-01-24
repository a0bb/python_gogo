from typing import Optional


class ArrayQueue:

    def __init__(self, capacity):
        self._capacity = capacity
        self._items = []
        self._head = 0
        self._tail = 0

    def enqueue(self, item: str) -> bool:
        if self._tail == self._capacity:
            # 表示队列已满
            if self._head == 0:
                return False
            else:
                # 如果没满，则进行数据搬移
                for i in range(0, self._tail - self._head):
                    self._items[i] = self._items[i + self._head]
                self._tail = self._tail - self._head
                self._head = 0
        # 这里为什么使用insert而不是使用append
        # 因为经历数据搬移之后，数据只是搬移并不是删除，这时候再append就会插入位置错误
        self._items.insert(self._tail, item)
        self._tail += 1
        return True

    def dequeue(self) -> Optional[str]:
        if self._head != self._tail:
            item = self._items[self._head]
            self._head += 1
            return item
        else:
            return None

    def __repr__(self):
        return ' '.join(item for item in self._items[self._head:self._tail])


if __name__ == '__main__':
    a = ArrayQueue(3)
    a.enqueue('a')
    a.enqueue('b')
    a.enqueue('c')

    a.dequeue()
    a.dequeue()

    a.enqueue('d')
    a.enqueue('e')

    print(a)


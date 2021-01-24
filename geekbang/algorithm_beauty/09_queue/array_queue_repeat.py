from typing import Optional


class ArrayQueue:

    def __init__(self, capacity):
        self._capacity = capacity
        self._item = []
        self._head = 0
        self._tail = 0

    def enqueue(self, item: str) -> bool:
        if self._capacity == self._tail:
            if self._head == 0:
                return False
            else:
                for i in range(self._tail - self._head):
                    self._item[i] = self._item[i + self._head]
                self._tail = self._tail - self._head
                self._head = 0

        self._item.insert(self._tail, item)
        self._tail += 1
        return True

    def dequeue(self) -> Optional[str]:
        if self._head == self._tail:
            return None
        value = self._item[self._head]
        self._head += 1
        return value

    def __repr__(self):
        return '->'.join(i for i in self._item[self._head: self._tail])


if __name__ == '__main__':
    queue = ArrayQueue(6)
    for i in range(10):
        queue.enqueue(str(i))

    print(queue)

    for i in range(4):
        queue.dequeue()

    print(queue)
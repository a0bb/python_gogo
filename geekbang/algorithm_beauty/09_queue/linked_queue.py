from typing import Optional


class Node:

    def __init__(self, data: str, next=None):
        self.data = data
        self._next = next


class LinkedQueue:

    def __init__(self):
        self._head: Optional[Node] = None
        self._tail: Optional[Node] = None

    def enqueue(self, value: str):
        new_node = Node(value)
        # 如果存在队尾，插入到队尾之后
        if self._tail:
            self._tail._next = new_node
        # 如果不存在队尾，插入到队首
        else:
            self._head = new_node
        # 只有一个元素的时候，队首=队尾
        self._tail = new_node

    def dequeue(self) -> Optional[str]:
        if self._head:
            value = self._head.data
            self._head = self._head._next
            # 如果没有self._head是空，则证明取出一个Node后，队列空了，那么需要把_tail值为空
            if not self._head:
                self._tail = None
            return value

    def __repr__(self):
        values = []
        current = self._head
        while current:
            values.append(current.data)
            current = current._next
        return '->'.join(v for v in values)


if __name__ == '__main__':
    l = LinkedQueue()
    l.enqueue('a')
    l.enqueue('b')
    l.enqueue('c')
    l.dequeue()

    print(l)

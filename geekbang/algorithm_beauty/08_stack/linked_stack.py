from typing import Optional


class Node:

    def __init__(self, data: int, next=None):
        self._data = data
        self._next = next


class LinkedStack:

    def __init__(self):
        self._top: Node = None

    def push(self, value: int):
        new_node = Node(value)
        new_node._next = self._top
        self._top = new_node

    def pop(self):
        if self._top:
            value = self._top._data
            self._top = self._top._next
            return value

    def __repr__(self):
        current = self._top
        nums = []
        while current:
            nums.append(current._data)
            current = current._next
        return ' '.join(f'{num} <-' for num in nums)


if __name__ == '__main__':
    stack = LinkedStack()
    for i in range(9):
        stack.push(i)
    print(stack)

    for _ in range(4):
        stack.pop()
    print(stack)

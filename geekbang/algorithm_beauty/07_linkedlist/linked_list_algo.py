from typing import Optional


class Node:

    def __init__(self, data: int, next: None):
        self.data = data
        self._next = next


def reverse(head: Node) -> Optional[Node]:
    reversed_head = None
    current = head
    while current:
        reversed_head, reversed_head._next, current = current, reversed_head, current._next
    return reversed_head

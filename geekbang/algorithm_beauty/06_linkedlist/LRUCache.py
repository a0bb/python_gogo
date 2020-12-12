class DBListNode(object):
    def __init__(self, x, y):
        self.key = x
        self.val = y
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.hkeys = {}
        # self.top和self.tail作为哨兵节点, 避免越界
        self.top = DBListNode(None, -1)
        self.tail = DBListNode(None, -1)
        self.top.next = self.tail
        self.tail.prev = self.top

    def get(self, key: int) -> int:
        if key in self.hkeys.keys():
            cur = self.hkeys[key]
            # 跳出原位置
            cur.next.prev = cur.prev
            cur.prev.next = cur.next
            # 最近用过的放到链表首部
            pre_top_node = self.top.next
            self.top.next = cur
            cur.prev = self.top
            cur.next = pre_top_node
            pre_top_node.prev = cur
            return self.hkeys[key].val

        return -1

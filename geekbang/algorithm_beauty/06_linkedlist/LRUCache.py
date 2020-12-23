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

    def put(self, key: int, value: int) -> None:
        if key in self.hkeys.keys():
            cur = self.hkeys[key]
            cur.val = value
            # 跳出原位置
            cur.next.prev = cur.prev
            cur.prev.next = cur.next
            # 放到头部
            pre_top_node = self.top.next
            cur.next = pre_top_node
            pre_top_node.prev = cur
            self.top.next = cur
            cur.prev = self.top
        else:
            # 增加新节点到头部
            cur = DBListNode(key, value)
            self.hkeys[key] = cur
            # 放到头部
            pre_top_node = self.top.next
            cur.next = pre_top_node
            pre_top_node.prev = cur
            self.top.next = cur
            cur.prev = self.top

            if len(self.hkeys.keys()) > self.cap:
                # 如果链表的长度大于定义长度，则删掉最后一个
                self.hkeys.pop(self.tail.prev.key)
                self.tail.prev.prev.next = self.tail
                self.tail.prev = self.tail.prev.prev

    def __repr__(self):
        vals = []
        p = self.top.next
        while p.next:
            vals.append(str(p.val))
            p = p.next
        return '->'.join(vals)


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache)
    cache.get(1)  # 返回  1
    cache.put(3, 3)  # 该操作会使得密钥 2 作废
    print(cache)
    cache.get(2)  # 返回 -1 (未找到)
    cache.put(4, 4)  # 该操作会使得密钥 1 作废
    print(cache)
    cache.get(1)  # 返回 -1 (未找到)
    cache.get(3)  # 返回  3
    print(cache)
    cache.get(4)  # 返回  4
    print(cache)
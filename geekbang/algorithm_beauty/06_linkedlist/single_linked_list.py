class Node:
    """ 链表结构的Node节点 """

    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next_node(self):
        return self.__next

    @next_node.setter
    def next_node(self, next_node):
        self.__next = next_node


class SingleLinkedList(object):

    def __init__(self):
        self.__head = None

    def find_by_value(self, value):
        node = self.__head
        while (node is not None) and (node.data != value):
            node = node.next_node
        return node

    def find_by_index(self, index):
        i = 0
        node = self.__head
        while (node is not None) and (i != index):
            node = node.next_node
            i += 1
        return node

    def insert_to_head(self, value):
        node = Node(value)
        node.next_node = self.__head
        self.__head = node

    def insert_after(self, node, value):
        if node is None:
            return
        new_node = Node(value)
        new_node.next_node = node.next_node
        node.next_node = new_node

    def insert_before(self, node, value):
        if node == self.__head:
            self.insert_to_head(value)
            return

        new_node = Node(value)
        pro = self.__head
        not_found = False
        while pro.next_node != node:
            if pro.next_node is None:
                not_found = True
                break
            else:
                pro = pro.next_node
        if not not_found:
            new_node.next_node = node
            pro.next_node = new_node

    def delete_by_node(self, node):
        if self.__head is None:
            return

        if node == self.__head:
            self.__head = node.next_node
            return

        pro = self.__head
        found = True
        while pro.next_node != node:
            if pro.next_node is None:
                found = False
                break
            else:
                pro = pro.next_node
        if found:
            pro.next_node = node.next_node
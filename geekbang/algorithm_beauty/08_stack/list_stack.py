

class Items:

    def __init__(self):
        self.data = []


class ListStack:

    def __init__(self):
        self.data = Items().data

    def push(self, value):
        self.data.insert(0, value)

    def pop(self):
        if self.data:
            self.data.pop(0)

    def __repr__(self):
        if self.data:
            return ' '.join([f'{i} <-' for i in self.data])


if __name__ == '__main__':
    stack = ListStack()
    for item in range(8):
        stack.push(item)
    print(stack)

    for _ in range(4):
        stack.pop()
    print(stack)

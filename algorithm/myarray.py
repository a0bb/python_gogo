"""
https://www.zhihu.com/question/44015086

"""


class MyArray:
    """A simple wrapper around List.
    You cannot have -1 in the array.
    """

    def __init__(self, capacity: int):
        self._data = []
        self._capacity = capacity

    # def __getitem__(self, position: int) -> object:
    #     return self._data[position]

    # def __setitem__(self, index: int, value: object):
    #     self._data[index] = value

    def __len__(self) -> int:
        return len(self._data)

    def __iter__(self):
        for item in self._data:
            yield item

    def find(self, index: int) -> object:
        try:
            return self._data[index]
        except IndexError:
            return None

    def delete(self, index: int) -> bool:
        try:
            self._data.pop(index)
            return True
        except IndexError:
            return False

    def insert(self, index: int, value: int) -> bool:
        if len(self) >= self._capacity:
            return False
        else:
            self._data.insert(index, value)

    def print_all(self):
        print(self)
        for item in self:
            print(item)


class Fib:
    def __init__(self, max):
        self.max = max
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib


def Fib2(m):
    a, b = 0, 1
    while True:
        if a > m:
            break
        yield a
        a, b = b, a + b


def test_myarray():
    array = MyArray(5)
    array.insert(0, 3)
    array.insert(0, 4)
    array.insert(1, 5)
    array.insert(3, 9)
    array.insert(3, 10)
    assert array.insert(0, 100) is False
    assert len(array) == 5
    assert array.find(1) == 5
    assert array.delete(4) is True
    array.print_all()


def test_fib():
    for item in Fib(20):
        print(item)


if __name__ == "__main__":
    # test_myarray()
    # test_fib()
    fib = Fib(13)
    for i in Fib2(13):
        print(i)


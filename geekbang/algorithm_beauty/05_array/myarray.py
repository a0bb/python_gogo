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

    def __getitem__(self, index: int) -> object:
        return self._data[index]

    def __setitem__(self, index: int, value: object):
        self._data[index] = value

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

    def insert(self, index: int, value: int) -> bool:
        if len(self) >= self._capacity:
            return False
        self._data.insert(index, value)
        return True

    def delete(self, index: int) -> bool:
        try:
            self._data.pop(index)
            return True
        except IndexError:
            return False

    def print_all(self):
        print(type(self))
        print(self)
        print(self._data)
        for item in self:
            print(item)


def test_myarray():
    array = MyArray(5)
    array.insert(0, 3)
    array.insert(0, 4)
    array.insert(1, 5)
    array.insert(3, 9)
    array.insert(3, 10)
    array.print_all()
    print('*' * 100)
    assert array.insert(0, 100) is False
    assert len(array) == 5
    assert array.find(1) == 5
    assert array.delete(4) is True
    array.print_all()


if __name__ == "__main__":
    test_myarray()


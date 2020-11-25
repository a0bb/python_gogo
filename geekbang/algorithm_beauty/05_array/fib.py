"""
__iter__
"""


class Fib:
    def __init__(self, max):
        self.max = max
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


def test_fib():
    for item in Fib(20):
        print(item)


if __name__ == '__main__':
    # test_fib()

    fib = Fib(13)
    for i in Fib2(13):
        print(i)

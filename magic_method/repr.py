
"""
重写object中的__repr__方法，达到自定义输出结果的目的

"""


class TestRepr:

    def __init__(self, input):
        self.input = input

    def __repr__(self):
        return f'input: {self.input}'


if __name__ == '__main__':
    t = TestRepr('abcde')
    print(t)

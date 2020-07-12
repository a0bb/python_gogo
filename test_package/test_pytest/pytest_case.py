import pytest


def func(x):
    return x


class TestFunc:
    def setup_module(self):
        print('>>>>> setup module')

    @classmethod
    def setup_class(cls):
        print('>>>>> setup class')

    def setup(self):
        print('setup')

    def teardown(self):
        print('teardown')

    def test_func_01(self):
        assert func(3) == 3

    def test_func_02(self):
        assert func(4) == 5

    @classmethod
    def teardown_class(cls):
        print('>>>>> teardown class')


if __name__ == '__main__':
    pytest.main()
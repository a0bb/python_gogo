import pytest


def func(x):
    return x


class TestFunc:

    @pytest.mark.parametrize("input, expect", [
        (5, 6), (7, 7), (8, 9)
    ])
    def test_01(self, input, expect):
        print('>>>>> test 01')
        assert func(input) == expect
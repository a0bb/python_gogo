import pytest


def func(x):
    return x


class TestFunc:

    @pytest.mark.fail
    def test_01(self):
        assert func(3) == 3

    @pytest.mark.fail
    def test_02(self):
        assert func(4) == 5



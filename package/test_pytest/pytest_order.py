
import pytest


class TestFunc:

    @pytest.mark.run(order=2)
    def test_order1(self):
        print("first test")
        assert True

    @pytest.mark.run(order=1)
    def test_order2(self):
        print("second test")
        assert True

    @pytest.mark.run(order=2)
    def test_order1(self):
        print("third test")
        assert True

    @pytest.mark.run(order=1)
    def test_order2(self):
        print("fourth test")
        assert True


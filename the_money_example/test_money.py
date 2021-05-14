import pytest

from money import Dollar


class TestMultiCurrencyMoney:
    def test_multiplication(self):
        five = Dollar(5)
        product = five.times(2)
        assert 10 == product.amount
        product = five.times(3)
        assert 15 == product.amount



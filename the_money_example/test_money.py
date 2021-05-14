import pytest

from money import Dollar


class TestMultiCurrencyMoney:
    def test_multiplication(self):
        # In the book, Kent Beck compares the two class instances
        # for equality. In Python we can only do those by defining
        # an __eq__ method, so to keep as close to the example as
        # possible I've chosen to compare the specific attributes.
        five = Dollar(5)
        assert Dollar(10).amount == five.times(2).amount
        assert Dollar(15).amount == five.times(3).amount

    def test_equality(self):
        assert Dollar(5).equals(Dollar(5))
        assert not Dollar(5).equals(Dollar(6))



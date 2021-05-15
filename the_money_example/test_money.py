import pytest

from money import Money, Bank


class TestMultiCurrencyMoney:
    def test_multiplication(self):
        five = Money.dollar(5)
        assert Money.dollar(10) == five.times(2)
        assert Money.dollar(15) == five.times(3)

    def test_equality(self):
        assert Money.dollar(5) == (Money.dollar(5))
        assert not Money.dollar(5) == (Money.dollar(6))
        assert not Money.franc(5) == (Money.dollar(5))

    def test_currency(self):
        assert 'USD' == Money.dollar(1).currency
        assert 'CHF' == Money.franc(1).currency
    
    def test_simple_addition(self):
        total = Money.dollar(5).plus(Money.dollar(5))
        assert Money.dollar(10) == total

        five = Money.dollar(5)
        total = five.plus(five)
        bank = Bank()
        reduced = bank.reduce(total, 'USD')
        assert Money.dollar(10), reduced

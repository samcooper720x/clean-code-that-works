import pytest

from money import Money, Dollar, Franc


class TestMultiCurrencyMoney:
    def test_dollar_multiplication(self):
        five = Money.dollar(5)
        assert Money.dollar(10).amount == five.times(2).amount
        assert Money.dollar(15).amount == five.times(3).amount

    def test_franc_multiplication(self):
        five = Money.franc(5)
        assert Money.franc(10).amount == five.times(2).amount
        assert Money.franc(15).amount == five.times(3).amount

    def test_equality(self):
        assert Money.dollar(5).equals(Money.dollar(5))
        assert not Money.dollar(5).equals(Money.dollar(6))
        assert Money.franc(5).equals(Money.franc(5))
        assert not Money.franc(5).equals(Money.franc(6))
        assert not Money.franc(5).equals(Money.dollar(5))
        assert Money(10, 'CHF').equals(Franc(10, 'CHF'))

    def test_currency(self):
        assert 'USD' == Money.dollar(1).currency
        assert 'CHF' == Money.franc(1).currency


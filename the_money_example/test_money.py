import pytest

from money import Money, Bank, Total


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
        five = Money.dollar(5)
        total = five.plus(five)
        bank = Bank()
        reduced = bank.reduce(total, 'USD')
        assert Money.dollar(10) == reduced

    def test_plus_returns_total(self):
        five = Money.dollar(5)
        total = five.plus(five)
        assert five == total.augend
        assert five == total.addend

    def test_reduce_total(self):
        total = Total(Money.dollar(3), Money.dollar(4))
        bank = Bank()
        result = bank.reduce(total, 'USD')
        assert Money.dollar(7) == result
    
    def test_reduce_money_different_currency(self):
        bank = Bank()
        bank.add_rate('CHF', 'USD', 2)
        result = bank.reduce(Money.franc(2), 'USD')
        assert Money.dollar(1), result

    def test_identity_rate(self):
        assert 1 == Bank().rate('USD', 'USD')

    # TODO use fixtures to reduce duplication in following tests.
    def test_mixed_addition(self):
        five_bucks = Money.dollar(5)
        ten_francs = Money.franc(10)
        bank = Bank()
        bank.add_rate('CHF', 'USD', 2)
        result = bank.reduce(five_bucks.plus(ten_francs), 'USD')
        assert Money.dollar(10) == result

    def test_total_plus_money(self):
        five_bucks = Money.dollar(5)
        ten_francs = Money.franc(10)
        bank = Bank()
        bank.add_rate('CHF', 'USD', 2)
        total = Total(five_bucks, ten_francs).plus(five_bucks)
        result = bank.reduce(total, 'USD')
        assert Money.dollar(15) == result

    def test_total_times(self):
        five_bucks = Money.dollar(5)
        ten_francs = Money.franc(10)
        bank = Bank()
        bank.add_rate('CHF', 'USD', 2)
        total = Total(five_bucks, ten_francs).times(2)
        result = bank.reduce(total, 'USD')
        assert Money.dollar(20) == result

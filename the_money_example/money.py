class Money:
    def __init__(self, amount, currency):
        self.currency = currency
        self.amount = amount

    @staticmethod
    def dollar(amount):
        return Dollar(amount, 'USD')

    @staticmethod
    def franc(amount):
        return Franc(amount, 'CHF')

    def equals(self, other):
        # Update comparison to ensure equality between classes and amounts.
        return self.amount == other.amount and \
               self.currency == other.currency

    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency)


class Dollar(Money):
    currency = 'USD'


class Franc(Money):
    currency = 'CHF'


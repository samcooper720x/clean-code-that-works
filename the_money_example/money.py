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
               type(self).__name__ == type(other).__name__


class Dollar(Money):
    def times(self, multiplier):
        return Money.dollar(self.amount * multiplier)


class Franc(Money):
    def times(self, multiplier):
        return Money.franc(self.amount * multiplier)


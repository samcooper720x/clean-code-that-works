class Money:
    def __init__(self, amount, currency):
        self.currency = currency
        self.amount = amount

    @staticmethod
    def dollar(amount):
        return Money(amount, 'USD')

    @staticmethod
    def franc(amount):
        return Money(amount, 'CHF')

    def equals(self, other):
        # Update comparison to ensure equality between classes and amounts.
        return self.amount == other.amount and \
               self.currency == other.currency

    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency)


class Money:
    def __init__(self, amount, currency):
        self.currency = currency
        self.amount = amount

    def __eq__(self, other):
        return (
            self.currency == other.currency and
            self.amount == other.amount
        )

    @staticmethod
    def dollar(amount):
        return Money(amount, 'USD')

    @staticmethod
    def franc(amount):
        return Money(amount, 'CHF')

    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency)
    


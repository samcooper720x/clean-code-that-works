class Money:
    def __init__(self, amount, currency):
        self._currency = currency
        self.amount = amount

    @property
    def currency(self):
        return self._currency

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
        return Money(self.amount * multiplier, self._currency)
    
    def plus(self, addend):
        return Total(self, addend)

    def reduce(self, to):
        return self


class Bank:
    def reduce(self, source, to):
        return source.reduce(to)


class Total:
    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend

    def reduce(self, to):
        amount = self.augend.amount + self.addend.amount
        return Money(amount, to)


class Money:
    def __init__(self, amount):
        self.amount = amount

    def equals(self, other):
        # Update comparison to ensure equality between classes and amounts.
        return self.amount == other.amount and \
               type(self).__name__ == type(other).__name__


class Dollar(Money):
    def times(self, multiplier):
        return Dollar(self.amount * multiplier)


class Franc(Money):
    def times(self, multiplier):
        return Franc(self.amount * multiplier)


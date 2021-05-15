class Money:
    # Although Kent Beck made his Java imp. of Money an abstract class
    # this was unnecessary in Python, I think due to it's use of
    # duck typing.
    def __init__(self, amount):
        self.amount = amount

    @staticmethod
    def dollar(amount):
        return Dollar(amount)

    @staticmethod
    def franc(amount):
        return Franc(amount)

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


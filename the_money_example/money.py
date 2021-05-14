class Dollar:
    def __init__(self, amount):
        # Although in the book Kent Beck eventually makes the amount
        # instance variable private, he is working in Java. Doing so
        # here in Python didn't seem appropiate. 
        self.amount = amount 

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)

    def equals(self, other):
        return self.amount == other.amount


class Franc:
    def __init__(self, amount):
        # Although in the book Kent Beck eventually makes the amount
        # instance variable private, he is working in Java. Doing so
        # here in Python didn't seem appropiate. 
        self.amount = amount 

    def times(self, multiplier):
        return Franc(self.amount * multiplier)

    def equals(self, other):
        return self.amount == other.amount



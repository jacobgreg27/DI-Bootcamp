def print_builtin_functions():
    """
    Prints the results of the abs(), int(), and input().

    The abs() function returns the absolute value of a number.
    The int() function converts a string or float to an integer.
    The input() function prompts the user to enter a string and returns the string.

    """
    print(abs(-5))
    print(int(3.14))
    print(input("Enter a string: "))

print(print_builtin_functions.__doc__)



# ------------------------EX 2-----------------------------

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f"{self.amount} {self.currency}"

    def __int__(self):
        return self.amount

    def __repr__(self):
        return f"{self.amount} {self.currency}"

    def __add__(self, other):
        if isinstance(other, Currency) and self.currency != other.currency:
            raise TypeError("Cannot add between Currency types")
        elif isinstance(other, Currency):
            return Currency(self.currency, self.amount + other.amount)
        else:
            return Currency(self.currency, self.amount + other)

    def __iadd__(self, other):
        if isinstance(other, Currency) and self.currency != other.currency:
            raise TypeError("Cannot add between Currency types")
        elif isinstance(other, Currency):
            self.amount += other.amount
        else:
            self.amount += other
        return self
    
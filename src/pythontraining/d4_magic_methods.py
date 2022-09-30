from functools import total_ordering


@total_ordering
class BankAccount():

    def __init__(self, name, height):
        self.name = name
        self.height = height

    def __str__(self):
        return f"Bank account of {self.name}"

    def __repr__(self):
        return f"BankAccount({self.name}, {self.height})"

    def __gt__(self, other):
        return self.height > other.height

account_john = BankAccount("John", 180)
account_tijn = BankAccount("Tijn", 182)
print(account_john)
print(account_tijn)
print(account_tijn > account_john)
print(account_tijn == account_john)
print(account_tijn < account_john)
"""
Type hinting exercise with classes
"""


def main() -> None:
    """Simple program for illustrative purposes"""
    name = ask_name()
    my_account = BankAccount(name)
    my_account.deposit(1000000000)
    my_account.withdraw(5000)
    my_account.print_balance()


def ask_name():
    """Return user input"""
    name = input("What is your name? ")
    return name


class BankAccount:
    """Simple class for bank accounts"""

    def __init__(self, owner: str):
        """Initialise account (balance 0)"""
        self.owner = owner
        self.balance = 0

    def deposit(self, amount: int):
        """Add money to the account"""
        self.balance += amount

    def withdraw(self, amount: int):
        """Withdraw money from the account"""
        self.balance -= amount

    def print_balance(self):
        """Prints full sentence"""
        print(f"Your account has €{self.balance:,}")


if __name__ == "__main__":
    main()

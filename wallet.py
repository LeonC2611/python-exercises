class Wallet:
    def __init__(self, balance=0):
        if not isinstance(balance, (int, float)):
            raise ValueError("Balance must be an integer or float")
        elif balance < 0:
            raise ValueError("Balance must not be negative")
        self._balance = balance

    # Message that displays the current balance in dollars to 2 decimal places
    def __str__(self):
        return f"Here is your balance: ${self._balance:.2f}"

    # Method to deposit amounts into balance instance variable
    def deposit(self, amount):
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be an int or float")
        elif amount < 0:
            raise ValueError("Amount can't be a negative number")
        else:
            self._balance += amount

    # Method to withdraw amounts from balance instance variable
    def withdraw(self, amount):
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be an int or float")
        elif amount < 0:
            raise ValueError("Amount can't be a negative number")
        elif self._balance - amount < 0:
            raise ValueError(
                f"Can't withdraw that amount. Here is your balance {self._balance}"
            )
        else:
            self._balance -= amount

    # balance property to use later if needed
    @property
    def balance(self):
        return self._balance


wallet = Wallet()

wallet.deposit(4)
wallet.withdraw(3)
print(wallet)

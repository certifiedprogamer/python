class BankAccount:
    def __init__(self, owner: str, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("No.")
        else:
            self.balance -= amount


account = BankAccount("Alice")
account.deposit(100)
account.withdraw(30)
print(account.balance)

#2 part 2

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Ви поповнили рахунок на : {amount} грн")
        self.print_balance()

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Ви зняли з рахунку: {amount} грн")
        else:
            print("Недостатньо коштів на рахунку для зняття готівки")
        self.print_balance()

    def print_balance(self):
        print(f"Поточний баланс: {self.balance} грн")

account = BankAccount("666")
account.print_balance()

account.deposit(666666)
account.withdraw(123000)
account.withdraw(1000000000)

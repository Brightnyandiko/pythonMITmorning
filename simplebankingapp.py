# Banking app. you have different type of bank accounts such as
# "savings account" and "checking account".
# both of these types of account share some common properties and
# trait/behaviours but also have specific features to each type.

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawn {amount}.New balance {self.balance}")
        else:
            print("insufficient balance")

    def display_balance(self):
        print(f"Account {self.account_number} balance:{self.balance}")

# child class
class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)
        self.interest_rate = 0.03

    def calculate_interest(self):
        return self.balance * self.interest_rate

    def display_balance(self):
        super().display_balance()
        print(f"interest earned : {self.calculate_interest()}")


class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)
        self.overdraft_limit = 2000.0

    def withdraw(self, amount):
        if self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
            print(f"Withdrawn {amount}.New balance {self.balance}")
        else:
            print("Insufficient amount")


savings_acc = SavingsAccount("ECFTSD", 1500.0)
checking_acc = CheckingAccount("GF4567", 2000.0)

savings_acc.deposit(690.0)
savings_acc.display_balance()

checking_acc.withdraw(900.0)
checking_acc.display_balance()

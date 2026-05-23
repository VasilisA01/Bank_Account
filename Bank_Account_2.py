class BankAccount:
    def __init__(self, owner_name, account_number, balance):
        self.Holder_Name = owner_name
        self.Account_Number = account_number
        self.Balance = balance

    def deposit(self, amount):
        self.Balance += amount
        print(f"Deposited {amount} $ Succesfully")

    def withdraw(self, amount):
        self.Balance -= amount
        print(f"Withdrawn {amount} $ Successfully")

    def get_balance(self):
        print(f"Your balance is: {self.Balance}")
        
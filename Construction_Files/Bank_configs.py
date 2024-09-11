from User_configs import User, mohiz

'''
BANK ACCOUNT ASSOCIATED WITH USER
1.  Stores detail about the account balance.
2.  Stores detail about the amount.
3.  Withdraw amount
4.  Deposit amount
5.  Transfer to other accounts

'''
class BankAccount:

    accounts = []

    def __init__(self,user: User):
        self.user = user
        self.balance = 0
        self.transactions = []


    def deposit(self, amount):

        self.balance += amount
        print("Balance after the deposit:", self.balance)
        self.transactions.append({"Transaction_type":"deposit","Amount":self.balance})


    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawn amount: {amount}")
            self.transactions.append({"Transaction_type": "Withdraw", "Amount": amount})
            print(f"New balance after withdraw: {self.balance}")
        else:
            print("Insufficient balance")

    def view_balance(self):
        print(f"Your account balance: {self.balance}")


My_account = BankAccount(mohiz)
My_account.deposit(1234456)
My_account.view_balance()
My_account.withdraw(4456)
My_account.view_balance()

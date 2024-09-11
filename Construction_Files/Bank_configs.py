from User_configs import User
from Transaction_Configs import Transaction
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

    def __init__(self,User):
        self.User = User
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):

        self.balance += amount
        print("Balance after the deposit:", self.balance)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawn amount: {amount}")
            print(f"New balance after withdraw: {self.balance}")
        else:
            print("Insufficient balance")

    def view_balance(self):
        print(f"Your account balance: {self.balance}")

    #Function to call user by its account number in class object
    def find_account_by_number(self, account_number):
        for account in BankAccount.accounts:
            if account.account_number == account_number:
                return account
        return None

    #TRNSFERING AMOUNT
    def transfer(self, amount, target_account_number):
        target_account = self.find_account_by_number(target_account_number)
        if target_account:
            if self.balance >= amount:
                self.balance -= amount
                target_account.balance += amount
                transaction = Transaction(amount, target_account_number)
                self.transactions.append(transaction)
                target_account.transactions.append(transaction)
                print("Transfer successful!")
            else:
                print("Insufficient funds for transfer.")
        else:
            print("Target account not found.")


My_account = BankAccount(12)
My_account.deposit(1234456)
My_account.view_balance()
My_account.withdraw(4456)
My_account.view_balance()

'''
This is my programmed BANKING SYSTEM
1.PARENT CLASS = USER:-
holds the detail about user
show details

2.CHILD CLASS = BANK
stores detail about the account balance.
stores detail about the amount.
Withdraw amount
Deposit amount
Transfer to other accounts

3.CLASS TRANSACTIONS
Tell the transaction details
amount recieved
and show the time date of transaction

Going to modify and extend more functions soon.
'''

#PARENT CLASS
import datetime
class User:
    def __init__(self, name, account_number, age, gender):
        self.name = name
        self.account_number = int(account_number)
        self.age = age
        self.gender = gender

    def show_details(self):
        print("-------------------------------------")
        print("Name of the customer is:", self.name)
        print("Account number:", self.account_number)
        print("Age of the customer is:", self.age)
        if self.gender == "M":
            print("Gender: Male")
        elif self.gender == "F":
            print("Gender: Female")
        else:
            print("Invalid gender detail given")

#Child Class
class Bank(User):
    accounts = []

    def __init__(self, name, account_number, age, gender):
        super().__init__(name, account_number, age, gender)
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
        for account in Bank.accounts:
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


class Transaction:
    def __init__(self, amount, target_account_number):
        self.amount = amount
        self.target_account_number = target_account_number
        self.timestamp = datetime.datetime.now()

    def display_details(self):
        print("Transaction details of: ", self.target_account_number)
        print("Amount Recieved:", self.amount)
        print("Transaction Time:", self.timestamp)


#Calling classes
user1 = Bank("Abmohiz", 2344, 22, "M")
user2 = Bank("Khan", 2222, 22, "M")

#ADDING USERS TO BANK
Bank.accounts = [user1, user2]

user1.show_details()
user2.show_details()

user1.deposit(30003)
user2.deposit(30003)

user1.withdraw(1000)
user1.view_balance()

user1.transfer(2000, 2222)
user1.view_balance()

# Display transaction details
for transaction in user1.transactions:
    transaction.display_details()

# for transaction in user2.transactions:
#     transaction.display_details()
import datetime
from Bank_configs import My_account


'''
Tell the transaction details
amount recieved
and show the time date of transaction

'''
class Transaction:

    def __init__(self,transactions):
        self.transactions = transactions
    def display_details(self):
        for transaction in self.transactions:
            transaction_type = transaction["Transaction_type"]
            amount = transaction["Amount"]
            timestamp = datetime.datetime.now()
            print(f"Transaction Type: {transaction_type}, Amount: {amount}, Time: {timestamp}")


transaction_history = Transaction(My_account.transactions)
transaction_history.display_details()
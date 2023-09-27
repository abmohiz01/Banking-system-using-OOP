# import pytest
from Bankingsystem2 import Bank

'''Testing deposited function'''
def test_deposit():
    # Create a Bank instance
    user = Bank("John", 10001, 25, "M")

    # Deposit some amount
    user.deposit(1000)

    # Check if the balance is updated correctly
    assert user.balance == 1000
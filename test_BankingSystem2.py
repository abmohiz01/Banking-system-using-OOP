import pytest
from Bankingsystem2 import Bank, Transaction
import datetime

@pytest.fixture
def bank_instance():
    '''fixture created for a user named jhon set some credentials
    and then testing functions on it '''
    # Create and return a Bank instance
    return Bank("John", 10001, 25, "M")

def test_deposit(bank_instance):
    '''This test function test the deposit function if it updates the balance or not
    And yes it does. If you deposit 1000 then it expect balance to be 1000, if you deposit multiple then
    It will check the balance and give assertion error if balance is not equal to its total desposited balance..
    '''
    # The 'bank_instance' fixture is automatically passed to this test
    bank = bank_instance

    # Deposit some amount
    bank.deposit(1000)
    bank.deposit(1000)
    # bank.deposit(1000)

    # Check if the balance is updated correctly
    assert bank.balance == 2000

def test_withdraw(bank_instance):
    '''This test function tests wether the amount withdraws from the deposited amount or not
    First it will deposit amount and then you will withdraw it
    after that if u check wether the amount is deducted or not you have to assert according to the
    result for instance
    deposit =1000, withdraw = 500, assert bank. balance == 500'''

    bank = bank_instance
    bank.deposit(1000)
    bank.withdraw(500)

    assert bank.balance == 500
    bank.view_balance()

def test_transaction():
    '''This test function test the transaction of amounts to another account'''
    transaction = Transaction(1000, 10001)
    assert transaction.amount == 1000
    assert transaction.target_account_number == 10001
    assert isinstance(transaction.timestamp, datetime.datetime)



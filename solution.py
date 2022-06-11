# Implementation for: https://github.com/romeoplatoon/oop-bank-accounts
# Optional requirements and Checkings account left as an exercise to the student.

from argparse import ArgumentError
import csv

class Bank:
  def __init__(self):
    self.accounts = []

class Account:
  accounts = []

  def __init__(self, id, balance, open_date):
    if balance < 0:
      raise Exception('Negative Balance Unallowed')

    self.id = id
    # balance is an integer representing cents, i.e. 150 is $1.50
    self.balance = balance
    self.open_date = open_date

    Account.accounts.append(self)

  @classmethod
  def all_accounts(cls):
    return cls.accounts

  @classmethod
  def find(cls, id):
    for account in cls.accounts:
      if account.id == id:
        return account

  def withdraw(self, amount):
    # Enough money in account to withdraw
    if amount < self.balance:
      self.balance -= amount
    else:
      print('Cannot withdraw more than current balance of account.')

    print(f'Current balance: {self.balance}')
    return self.balance

  def deposit(self, amount):
    self.balance += amount


my_bank = Bank()

with open('support/accounts.csv', newline='') as csvfile:
  reader = csv.DictReader(csvfile, fieldnames=['id', 'balance', 'open_date'])
  for row in reader:
    # print(row)

    balance = int(row['balance'])
    new_account = Account(row['id'], balance, row['open_date'])
    my_bank.accounts.append(new_account)


class Savings(Account):
  def __init__(self, id, balance, open_date):
    # balance must be at least $10
    if balance < 1000:
      raise ArgumentError('Initial balance must be at least $10')
    else:
      parent = super()
      parent.__init__(id, balance, open_date)

  def withdraw(self, amount):
    # $2 transaction fee
    # balance can never be less than $10

    # Customer able to withdraw funds
    if (self.balance - amount) > 1200:
      self.balance -= (amount + 200)
    else:
      print('Must have minimum of $10 in account plus $2 transaction fee.')

    print(f'Current balance: {self.balance}')
    return self.balance

  # interest rate must be a decimal < 1
  def add_interest(self, interest_rate):
    interest_earned = self.balance * interest_rate
    self.balance = self.balance + interest_earned
    return interest_earned

# Tests
#print(my_bank.accounts)
#print(Account.find('1212').id)
# my_account = Account(1, 5, '1994-11-17 14:04:56 -0800')
# my_account.withdraw(10) # warning, trying to withdraw too much
# my_account.withdraw(1) # successful withdraw


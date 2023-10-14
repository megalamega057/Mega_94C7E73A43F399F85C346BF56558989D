'''Implement a class called BankAccount that represents a bank account.The class should have private
attributes for account number,account holder name,and account balance.Include methods to 
deposit money,withdraw money and display the account balance.Ensure that the account balance 
cannot be accesed directly from outside the class.Write a program to create an instance of the
BankAccount class and tedt the deposit and withdrawl functionality'''


class BankAccount:

def __init__(self,account_number,account_holder_name,initial_balance=0.0):
  self.__acount_number = account_number
  self.__account_holder_name = account_holder_name
  self.__account__balance = initial_balance

def deposit(self, amount):
  if amount > 0:
    self.__account_balance += amount
    #self.account_balance = self_Account_balance=amount
    print("Deposited ₹{}. New balance:₹{}"format(amount,
                                            self._account_balance))
  else:
    print("Invalid deposit amount. please deposit a positive amount.")

def withdraw(self, amount):
  if amount > 0 and amount <= self.__account_balance:
    self.__account_balance -= amount
    #self__account_balance = self_account_balance- amount
  print("Withdrew ₹{}. New balance: ₹{}".format(amount,
                                            self.__account_balance))
else:
 print("Invalid withdrawl amount or insufficient balance.")

def display_balance(self):
  print("account balance for {} (Account #{}): ₹{}".format(
    self.__account_holder_name, self.__account_number,
    self.__account_balance))
  

#create an instance of the BankAccount class
account = BankAccount(account_number="123456789",
                      ,account_holder_name="Hari prabhu",
                      initial_balance=5000.0)

# Test deposit and withdrawl functionality
account.display_balance()
account.deposit(500.0)
account.withdrawl(200.0)
account.display balance()

  
#  Requirements
"""
Account number
Account name/user
Deposite
Withdrawal
Balance
"""
# Actions by User
'''
Deposite
Withdrawal
'''
import sys

class Bank:
    bank_name = "OTUODI bank"

    def __init__(self, account_num, account_name, initial_bal = 0):
        self.account_num = account_num
        self.account_name = account_name
        self.initial_bal = initial_bal
    
    def withdraw(self, amount):
        self.amount = amount
        if self.amount >= self.initial_bal:
            print("Insufficient fund.")
            sys.exit()

        self.initial_bal -= self.amount
        print("Current balance: ", self.initial_bal)

    def deposit(self, amount):
        self.amount = amount
        self.initial_bal += self.amount
        print("Current balance: ", self.initial_bal) 


print("Welcome to", Bank.bank_name)
account_name = input("Enter your name: ")
account_num = int(input("Enter your account number: "))

banker  = Bank(account_name, account_num)
while True:
    print("Choose\n A to Deposit\n B to Withdraw\n E to Exit")
    
    choice = input("Enter option: ")

    if choice == "a":
        amount = float(input("Enter amount you want to deposit")) 
        banker.deposit(amount)
    elif choice == "b":
        amount = float(input("Enter amount you want to withdraw"))  
        banker.withdraw(amount)
    elif choice == "e":
        print("Try again")
        sys.exit()
    else:
        print("Incorrect data entered.")
        print("Exit")
        
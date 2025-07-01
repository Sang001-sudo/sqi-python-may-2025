# Scenario: You want to create a bank account that supports deposits and withdrawals.
# Task: Create a bank account class that has two attributes:
# owner
# balance

# and two methods:
# deposit
# Withdraw

# Withdrawals may not exceed the available balance.
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account 
# can't be overdrawn.

# You are not expected to use the input function, just pass in values for the amounts into 
# the methods directly, no need for loops either.
# See the next slide for a sample execution of the code you will write.

class Account:
    def __init__(self, owner:str, balance:float):
        self.owner = owner
        self.balance = balance


    def deposit(self, amount:int):
        if amount < 1:
            print("Not cool")
            return
        print("Deposit Accepted")

    def withdraw(self, amount:int):
        if amount < 1 or amount > self.balance:
            print("Funds Unavailable!")
            return
        print("Withdrawal Accepted")

    def __str__(self): # type: ignore
        print(f"Account owner: {self.owner}\nAccount balance: ${self.balance}")

#1. Instantiate the class
acct1 = Account('Winnie', 100)

#2. Print the object
print(acct1)
# Output:
# Account owner: Winnie
# Account balance: $100

#3. Show the account owner attribute
print(acct1.owner)  # Winnie

#4. Show the account balance attribute
print(acct1.balance)  # 100

#5. Make a series of deposits and withdrawals
acct1.deposit(50)  # Output: Deposit Accepted

acct1.withdraw(15)  # Output: Withdrawal Accepted

#6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)  # Output: Funds Unavailable!

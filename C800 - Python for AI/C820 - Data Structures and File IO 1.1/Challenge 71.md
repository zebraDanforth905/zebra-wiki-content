---
title: "Challenge #71: Overriding - Create a banking program"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 71
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #71: Overriding - Create a banking program

## Problem

Your challenge is to create a banking program

Create a class called BankAccount

• There should be methods for depositing funds and withdrawing funds

• There should be properties for the account holders name, balance, date of birth, social insurance number, phone number, and pin

• Create some user-intractability, allow users to create accounts, look up their balance, make withdrawals and deposits, change their pin, change their phone number

Also create a file system to allow you to maintain the bank account in between uses of the program.

## Solutions

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            print("Deposited $" + str(amount))
        else:
            print("You can only deposit a positive amount.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money in the account.")
        else:
            self.balance = self.balance - amount
            print("Withdrew $" + str(amount))

    def __str__(self):
        return self.owner + "'s account: $" + str(self.balance)


account = BankAccount("Sam", 100)

option = 0
while option != 4:
    print("\n" + str(account))
    print("1) Deposit")
    print("2) Withdraw")
    print("3) Check balance")
    print("4) Exit")
    option = int(input("Choose an option: "))

    if option == 1:
        account.deposit(int(input("How much to deposit? ")))
    elif option == 2:
        account.withdraw(int(input("How much to withdraw? ")))
    elif option == 3:
        print("Your balance is $" + str(account.balance))
    elif option == 4:
        print("Goodbye!")
    else:
        print("Invalid option!")
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

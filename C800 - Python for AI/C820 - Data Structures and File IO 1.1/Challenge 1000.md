---
title: "Challenge #1000: Build Your Own Banking Program"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 1000
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #1000: Build Your Own Banking Program

## Problem

Objective:

You will design and create a console-based banking program using Python and object-oriented programming. Your program will simulate a bank, allowing customers to create accounts, deposit and withdraw money, transfer funds, and keep track of all transactions. You will use classes, inheritance, and methods to organize your program.

Part 1: Create Your Account Classes

Students need to design a base class and at least three specialized account types:

•
BankAccount (Base Class)

• Attributes:

• Account number

• Account holder name

• Balance

• Transaction history (a collection of Transaction objects)

• Methods:

•
deposit(amount) – add money

•
withdraw(amount) – remove money

•
get_balance() – show current balance

•
display_account_info() – show account details

•
SavingsAccount (inherits BankAccount)

• Represents a savings account that earns interest.

• Additional method:

•
apply_interest() – calculate and add interest to the balance

•
CheckingAccount (inherits BankAccount)

• Represents an account for everyday spending.

• Additional feature:

• Allow overdraft: withdrawals can go beyond the current balance up to a limit

•
BusinessAccount (inherits BankAccount)

• Represents a small business account.

• Additional features:

• Store a business name

• Add bonuses for large deposits

Tip: Use inheritance to avoid repeating code for common features like deposits, withdrawals, and balance display.

Part 2: Create a Transaction Class

•
Transaction is a separate class that stores information about each financial action.

• Attributes of a Transaction:

• Type: "deposit", "withdrawal", "transfer in", or "transfer out"

• Amount

• Date and time

• Each account should maintain a transaction history, which is a data structure of Transaction objects.

• Students can choose a data structure they find appropriate, such as a list, dictionary, or queue, to store the transactions.

Banking Context:
Banks record every deposit, withdrawal, and transfer. Transaction histories help customers track their money and prevent mistakes.

Part 3: Implement a Menu System

Your program should have a console menu that allows users to choose actions:

• Create a new account

• Deposit money

• Withdraw money

• Apply interest (SavingsAccount only)

• Transfer money between accounts

• View account details

• View transaction history

• Exit the program

Banking Context:
Menus simulate how real banks provide options for managing accounts. Students should design the menu so it repeats until the user chooses to exit.

Part 4: Add Realistic Banking Features

•
Input Validation

• Users cannot enter invalid amounts (negative numbers, letters instead of numbers).

• Withdrawals cannot exceed overdraft limits for CheckingAccounts.

•
Persistent Storage

• Save all account and transaction data to a file so it is not lost.

• Load data when the program starts.

•
Money Transfers Between Accounts

• Users can transfer money from one account to another.

• Transfers should also appear in both accounts’ transaction histories.

•
Account Search

• Users can find accounts by account number or holder name.

Part 5: Deliverables

• Python program files implementing accounts, transaction class, menu system, and all features.

• Example screenshots of the program running.

## Solutions

```python
# Add solution(s) here
```

You can include multiple approaches in this section if needed.

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

---
title: "Challenge #500: Trip Expense Calculator & Bill Splitter"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 500
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #500: Trip Expense Calculator & Bill Splitter

## Problem

Project Overview

You will create a Trip Expense Calculator for a group of friends going on a trip together.
Each person may spend money on different items such as food, transport, accommodation, or activities.

Your program will calculate how much everyone spent, find each person’s fair share, and suggest who should pay whom so that everyone ends up paying equally.

This project combines real-world logic with Python programming, testing your ability to use input/output, loops, dictionaries, and functions effectively.

Project Objectives

By completing this project, you will learn how to:

• Collect and process user input dynamically.

• Perform calculations using loops and dictionaries.

• Implement a greedy algorithm to minimize the number of payments.

• Display results neatly in a menu-driven interface.

• Modify and update data during program execution.

• Export the final results to a text file.

Key Technical Words Explained

Term
Meaning

Variable
A name that stores data (e.g., total_cost = 300).

Loop
Repeats a block of code, such as asking for multiple expenses.

Dictionary
A data structure that stores data in key-value pairs (e.g., "Alice": 120).

Function
A reusable block of code that performs a task (e.g., calculating balances).

Balance
The difference between how much someone spent and what they should have paid.

Greedy Algorithm
A step-by-step approach that always picks the best immediate option (like matching the biggest debtor with the biggest creditor).

Menu-driven interface
A program that shows a list of choices and lets the user select what to do next.

Exporting to a file
Writing results from the program into a .txt file so they can be saved or printed later.

Project Requirements

Input

• Ask for the number of participants.

• Ask for the name of each participant.

• Allow each participant to enter multiple expenses (e.g., food, transport, etc.).

• Stop accepting expenses when the participant types 'done'.

Processing

• Sum all expenses for each participant.

• Calculate total trip cost.

• Determine each person’s fair share (total cost ÷ number of participants).

• Calculate balances — how much each person owes or is owed.

• Suggest who should pay whom to settle balances using as few transactions as possible.

Output (Menu Options)

When the program finishes processing, it should display a menu that allows the user to:

•
Display the transaction table

• Show all transactions with clear column headings:
Transaction | Person | Amount

•
Change an amount

• Allow the user to update a specific person’s expense and automatically recalculate totals and balances.

• Show the total trip cost

• Show each person’s fair share and balance

•
Show suggested payments to balance expenses

•
Export results to a text file

• Save the full summary (totals, fair shares, balances, and suggested payments) into a file called something like trip_summary.txt.

• Exit the program

Understanding the Greedy Algorithm

When people owe each other money, there are many ways to settle debts.
The goal is to minimize the number of payments while making sure everyone pays their fair share.

A Greedy Algorithm solves this by following a simple idea:

• Find the person who owes the most (debtor) and the person who is owed the most (creditor).

• Have the debtor pay the creditor as much as possible (the smaller of the two amounts).

• Update their balances.

• Repeat until all balances are zero.

This method is called greedy because it always takes the best step at the moment.
It’s efficient and works very well for real-world money-splitting problems.

Example

Input Summary:

Number of participants: 3
Alice spends: 120
Bob spends: 60
Charlie spends: 90

Output (Menu Option 5 – Show Suggested Payments):

Total trip cost: $270.00
Each person's fair share: $90.00

Balances:
Alice: +$30.00
Bob: -$30.00
Charlie: $0.00

Suggested payments:
Bob pays Alice $30.00

Output (Menu Option 6 – Export Results):
A text file named trip_summary.txt should be created with the above summary inside.

## Solutions

```python
# Add solution(s) here
```

You can include multiple approaches in this section if needed.

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

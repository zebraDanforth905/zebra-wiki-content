---
title: "Challenge #500: Trip Expense Calculator & Bill Splitter"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 500
challenge_type: "regular"   # regular | supplemental | discontinued | optional | unnumbered
language: python
tags: [python]
author: "Your Name"
status: draft        # todo | draft | reviewed | final
---

# Challenge #500: Trip Expense Calculator & Bill Splitter

## Challenge Brief

https://lms.zebrarobotics.com/courses/2597/assignments/53232

## Solutions

```python
"""
Trip Expense Calculator and Bill Splitter.

A group of friends goes on a trip. Each person spends a different amount.
This program works out everyone's fair share, who owes money and who is owed,
and suggests a small set of payments so that everyone ends up paying equally.
The final report is also written to a text file.
"""


def get_expenses():
    spending = {}
    count = int(input("How many people are on the trip? "))
    for i in range(count):
        name = input("Enter a person's name: ")
        amount = float(input("How much did " + name + " spend? $"))
        spending[name] = amount
    return spending


def settle_up(spending):
    total = sum(spending.values())
    fairShare = total / len(spending)

    # A person's balance is what they spent minus their fair share.
    # Positive = they are owed money, negative = they owe money.
    balances = {}
    for name in spending:
        balances[name] = spending[name] - fairShare

    payments = []
    # Greedy: repeatedly match the biggest debtor with the biggest creditor.
    while True:
        debtor = min(balances, key=lambda n: balances[n])
        creditor = max(balances, key=lambda n: balances[n])

        if balances[debtor] >= -0.01 and balances[creditor] <= 0.01:
            break

        amount = min(-balances[debtor], balances[creditor])
        amount = round(amount, 2)
        payments.append((debtor, creditor, amount))
        balances[debtor] = balances[debtor] + amount
        balances[creditor] = balances[creditor] - amount

    return total, fairShare, payments


def main():
    spending = get_expenses()
    total, fairShare, payments = settle_up(spending)

    report = []
    report.append("===== Trip Expense Report =====")
    report.append("Total spent: $" + str(round(total, 2)))
    report.append("Fair share per person: $" + str(round(fairShare, 2)))
    report.append("")
    report.append("Suggested payments:")
    if len(payments) == 0:
        report.append("Everyone already paid their fair share!")
    else:
        for debtor, creditor, amount in payments:
            report.append(debtor + " pays " + creditor + " $" + str(amount))

    for line in report:
        print(line)

    outObj = open("trip_report.txt", "w")
    for line in report:
        outObj.write(line + "\n")
    outObj.close()
    print("\nReport saved to trip_report.txt")


main()
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

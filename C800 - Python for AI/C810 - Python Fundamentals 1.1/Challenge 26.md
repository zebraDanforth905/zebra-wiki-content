---
title: "Challenge #26: Random Money Action"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 26
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #26: Random Money Action

## Problem

Write a Python program that:

• Asks the user how much money they have (an integer)

• Generates a random integer between 1 and 5

• Uses a match statement to perform an action on the money based on the random number

• Prints the random number and the updated amount of money

Actions

Case
Action

1
Add $5

2
Subtract $3

3
Double your money

4
Halve your money (integer division)

5
Lose all your money (reset to $0)

Default
Print “No action”

Example Output

Enter your money: 10

Random number: 3

You now have $20

## Solutions

```python
import random

money = int(input("How much money do you have? "))
action = random.randint(1, 5)

match action:
    case 1:
        money = money + 10
        print("You found $10! You now have $" + str(money))
    case 2:
        money = money - 5
        print("You lost $5! You now have $" + str(money))
    case 3:
        money = money * 2
        print("You doubled your money! You now have $" + str(money))
    case 4:
        money = 0
        print("You lost it all! You now have $" + str(money))
    case 5:
        print("Nothing happened. You still have $" + str(money))
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

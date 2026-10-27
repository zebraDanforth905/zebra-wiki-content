---
title: "Challenge #15: Casting - Tax Calculator"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 15
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #15: Casting - Tax Calculator

## Problem

Write a program that takes the price of 3 items and adds them all together and prints the total price + tax.
You can assume that the prices are of type int, and tax is 15% of the total (so multiply by 1.15)
For example:

## Solutions

```python
item1 = int(input("Enter the price of item 1:"))
item2 = int(input("Enter the price of item 2:"))
item3 = int(input("Enter the price of item 3:"))

total = item1 + item2 + item3
total = total + total * 0.15

print("Your total is " + str(total))
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

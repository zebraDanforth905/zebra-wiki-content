---
title: "Challenge #05: Variables - Find the Error"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 5
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #05: Variables - Find the Error

## Problem

Figure out what is wrong (if there is something) in the following variable declarations:

Finding Errors in Variables

Variable Declaration

Describe the problem and fix it

name: “John Smith”

NAME = “John Smith”

I_dont_know = 13

numOfApples = 69

link_word = and

## Solutions

```python
# Challenge 5: Find the error in each variable declaration and fix it.

# 1) my name = "Sam"      -> variable names cannot have spaces
myName = "Sam"

# 2) 2ndPlace = "silver"  -> a variable name cannot start with a number
secondPlace = "silver"

# 3) age = 12             -> this one is correct
age = 12

# 4) price = "9.99        -> missing the closing quote
price = "9.99"

# 5) is-open = True       -> dashes are not allowed in variable names
isOpen = True

print(myName, secondPlace, age, price, isOpen)
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

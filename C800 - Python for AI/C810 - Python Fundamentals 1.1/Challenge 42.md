---
title: "Challenge #42: Functions - Max Number"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 42
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #42: Functions - Max Number

## Problem

Write a function named get_maximum that takes two numeric inputs and returns the larger of the two values.
Use clear and descriptive variable names, and ensure the function handles cases where both numbers are equal.

Example Behavior

get_maximum(10, 20)  ➝  20

get_maximum(5, 5)    ➝  5

Requirements

• Use meaningful function and parameter names.

• The function must return the greater value.

• If both values are equal, the function should return either one.

## Solutions

```python
def get_maximum(firstNumber, secondNumber):
    if firstNumber > secondNumber:
        return firstNumber
    else:
        return secondNumber


print(get_maximum(4, 9))
print(get_maximum(15, 3))
print(get_maximum(7, 7))
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

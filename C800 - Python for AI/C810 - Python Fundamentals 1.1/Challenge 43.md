---
title: "Challenge #43: Functions - Fizz Buzz"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 43
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #43: Functions - Fizz Buzz

## Problem

Create a function named fizz_buzz that accepts one number as input and returns:

•
"Fizz" if the number is divisible by 3

•
"Buzz" if the number is divisible by 5

•
"FizzBuzz" if the number is divisible by both 3 and 5

• The number itself if none of the above conditions apply

After defining the function, call it with three different numbers and print the results.

Example Behavior

fizz_buzz(3)      ➝ "Fizz"

fizz_buzz(5)      ➝ "Buzz"

fizz_buzz(15)     ➝ "FizzBuzz"

fizz_buzz(7)      ➝ 7

Requirements

• Use appropriate function and variable names.

• Ensure correct order of condition checks.

• Print the result for three sample inputs.

## Solutions

```python
def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number


print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))
print(fizz_buzz(7))
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

---
title: "Challenge #31: Number Guessing with Warnings"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 31
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #31: Number Guessing with Warnings

## Problem

Write a Python program that:

•
Generates a random number between 1 and 50.

• Allows the user to guess the number repeatedly using a while loop.

• Implements the following rules inside the loop:

• If the user enters a number less than 1 or greater than 50, print a warning and skip that iteration using continue.

• If the user guesses the correct number, print a congratulatory message and exit the loop using break.

• Otherwise, tell the user if the guess is too high or too low.

Hints

• Use import random and random.randint(1, 50) to generate the secret number.

• Use continue to handle invalid guesses (out of range).

• Use break to stop the loop when the user guesses correctly.

Example Run

Guess the number between 1 and 50: 60
Invalid input! Number must be between 1 and 50.

Guess the number between 1 and 50: -5
Invalid input! Number must be between 1 and 50.

Guess the number between 1 and 50: 25
Too low! Try again.

Guess the number between 1 and 50: 42
Congratulations! You guessed it!

## Solutions

```python
import random

number = random.randint(1, 50)
guess = 0

while guess != number:
    guess = int(input("Guess the number (1-50): "))
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("You got it! The number was " + str(number) + ".")
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

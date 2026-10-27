---
title: "Challenge #25: Branching Logic - Guessing Game"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 25
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #25: Branching Logic - Guessing Game

## Problem

Generate a random number between 1 and 5, and ask the user to guess the number. If the user guesses correctly, congratulate the user on guessing correctly; if not, wish them good luck next time.

You can generate a random number like this:

The code above generates a random number between 1 and 5; note that it will include the second number in the range. In general, here is how you use randint:

The following video provides more detail:

## Solutions

```python
import random

number = random.randint(1, 5)
guess = int(input("Guess a number between 1 and 5: "))

if guess == number:
    print("Correct! You guessed it!")
else:
    print("Sorry, the number was " + str(number) + ".")
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

- https://iframe.mediadelivery.net/embed/711340/85b12c86-1b94-4653-b22d-7873532294e8?autoplay=false&preload=false

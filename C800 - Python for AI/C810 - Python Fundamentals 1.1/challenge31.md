---
title: "Challenge #31: Number Guessing with Warnings"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 31
challenge_type: "regular"   # regular | supplemental | discontinued
language: python
tags: [python]
author: "Your Name"
status: draft        # todo | draft | reviewed | final
---

# Challenge #31: Number Guessing with Warnings

## Challenge Brief

https://lms.zebrarobotics.com/courses/2576/assignments/52691

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

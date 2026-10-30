---
title: "Challenge #25: Branching Logic - Guessing Game"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 25
challenge_type: "regular"   # regular | supplemental | discontinued
language: python
tags: [python]
author: "Your Name"
status: draft        # todo | draft | reviewed | final
---

# Challenge #25: Branching Logic - Guessing Game

## Challenge Brief

https://lms.zebrarobotics.com/courses/2576/assignments/52685

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

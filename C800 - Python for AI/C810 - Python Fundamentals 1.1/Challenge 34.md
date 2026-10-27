---
title: "Challenge #34: For Loops - Re-write"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 34
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #34: For Loops - Re-write

## Problem

Rewrite challenge 29, 30, and 31 using a FOR loop.

## Solutions

```python
# Challenge 34: Rewrite challenges 29, 30, and 31 using FOR loops.

# Challenge 29 with a for loop - 99 Bottles of Milk
for bottles in range(99, 0, -1):
    print(str(bottles) + " bottles of milk on the wall, " + str(bottles) + " bottles of milk.")
    print("Take one down and pass it around, " + str(bottles - 1) + " bottles of milk on the wall.")

# Challenge 30 with a for loop - Remove Vowels
sentence = input("Enter a sentence: ")
result = ""
for letter in sentence:
    if letter not in "aeiou":
        result = result + letter
print(result)

# Challenge 31 with a for loop - Number Guessing (5 tries)
import random
number = random.randint(1, 50)
for attempt in range(5):
    guess = int(input("Guess the number (1-50): "))
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("You got it!")
        break
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

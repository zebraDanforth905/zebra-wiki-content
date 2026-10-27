---
title: "Challenge #38: For Loops - Encryption II"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 38
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #38: For Loops - Encryption II

## Problem

This is the same as encryption 1 (challenge 37), but the first input from the user should tell how many characters need to be shifted; it can range from 1 to 25. In Encryption 1, you shifted all characters by 1 position; now the user can choose any number between 1 and 25, and the program should be able to shift and encrypt.

## Solutions

```python
shift = int(input("How many positions do you want to shift (1-25)? "))
sentence = input("Enter a sentence (lowercase letters and spaces only): ")

result = ""
for letter in sentence:
    if letter == " ":
        result = result + " "
    else:
        shifted = (ord(letter) - ord("a") + shift) % 26 + ord("a")
        result = result + chr(shifted)

print(result)
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

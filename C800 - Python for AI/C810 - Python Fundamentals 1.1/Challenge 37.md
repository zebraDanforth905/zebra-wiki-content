---
title: "Challenge #37: For Loops - Encryption"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 37
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #37: For Loops - Encryption

## Problem

Write a program to get a sentence from the user. Only lower case letters will be typed, except for a space character. Shift all the characters by 1 position.

For example – character ‘a’ should become ‘b’, ‘b’ should become ‘c’ and so on, with ‘z’ becoming to ‘a’.

e.g.
Input: “try to take road less traveled”
Output: “usz up ublf spbe mftt usbwfmfe”

Hint: Ask your coach to explain ASCII values to you. It will help a lot with this challenge.

## Solutions

```python
sentence = input("Enter a sentence (lowercase letters and spaces only): ")

result = ""
for letter in sentence:
    if letter == " ":
        result = result + " "
    else:
        shifted = (ord(letter) - ord("a") + 1) % 26 + ord("a")
        result = result + chr(shifted)

print(result)
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

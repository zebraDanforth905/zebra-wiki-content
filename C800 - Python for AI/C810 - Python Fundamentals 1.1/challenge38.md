---
title: "Challenge #38: For Loops - Encryption II"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 38
challenge_type: "regular"   # regular | supplemental | discontinued
language: python
tags: [python]
author: "Your Name"
status: draft        # todo | draft | reviewed | final
---

# Challenge #38: For Loops - Encryption II

## Challenge Brief

https://lms.zebrarobotics.com/courses/2576/assignments/52698

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

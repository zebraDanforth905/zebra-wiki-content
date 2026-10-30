---
title: "Supplemental Challenge #11: Dictionary - Letter Counter"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 11
challenge_type: "supplemental"   # regular | supplemental | discontinued
language: python
tags: [python]
author: "Your Name"
status: draft        # todo | draft | reviewed | final
---

# Supplemental Challenge #11: Dictionary - Letter Counter

## Challenge Brief

https://lms.zebrarobotics.com/courses/2576/assignments/52718

## Solutions

```python
text = input("Enter a string: ")

counts = {}
for letter in text:
    if letter == " ":
        continue
    letter = letter.lower()
    if letter in counts:
        counts[letter] = counts[letter] + 1
    else:
        counts[letter] = 1

print(counts)
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

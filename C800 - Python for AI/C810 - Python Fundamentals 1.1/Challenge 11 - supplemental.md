---
title: "Supplemental Challenge #11: Dictionary - Letter Counter"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 11
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "supplemental"
---

# Supplemental Challenge #11: Dictionary - Letter Counter

## Problem

Get a string from a user and then create a dictionary that keeps track of how many times each letter occurs in the string.

For example:

When given the string: “Hello World”

Create the dictionary: {“d”: 1,“e”: 1, “h”: 1, “l”:3, “o”: 2, “r”: 1, “w”: 1}

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

---
title: "Challenge #32: For Loops - Sentence Splitter"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 32
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #32: For Loops - Sentence Splitter

## Problem

Write a program to get a word from the user and display all of its characters separately.

For example:

Please enter a word: T-REX

T
-
R
E
X

## Solutions

```python
word = input("Please enter a word: ")

result = ""
for letter in word:
    result = result + letter + "-"

# remove the extra dash on the end
print(result[:-1])
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

---
title: "Challenge #35: For Loops - Multiplication Table"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 35
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #35: For Loops - Multiplication Table

## Problem

Get an input number from the user and print its multiplication table up til' 20.

For example:

Please enter a number: 2

2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40.

## Solutions

```python
number = int(input("Please enter a number: "))

for i in range(1, 21):
    print(number * i)
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

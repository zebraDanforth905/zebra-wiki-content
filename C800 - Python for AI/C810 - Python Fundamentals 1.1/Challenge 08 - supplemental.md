---
title: "Supplemental Challenge #08: Repeated Logic (While Loops) - Pyramids"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 8
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "supplemental"
---

# Supplemental Challenge #08: Repeated Logic (While Loops) - Pyramids

## Problem

Create a program that asks a user for a number and then uses it to create a pyramid like so:

For input 5, output:

*

**

***

****

*****

## Solutions

```python
number = int(input("Enter a number: "))

i = 1
while i <= number:
    print("*" * i)
    i = i + 1
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

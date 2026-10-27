---
title: "Supplemental Challenge #04: Type Casting and Numerical Operators - GPA Calculator"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 4
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "supplemental"
---

# Supplemental Challenge #04: Type Casting and Numerical Operators - GPA Calculator

## Problem

Ask a user for their grades, then tally them all up and calculate the average.

## Solutions

```python
howMany = int(input("How many grades do you have? "))

total = 0
for i in range(howMany):
    grade = float(input("Enter a grade: "))
    total = total + grade

average = total / howMany
print("Your average grade is " + str(average))
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

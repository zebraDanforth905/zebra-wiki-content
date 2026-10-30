---
title: "Supplemental Challenge #4: Type Casting and Numerical Operators - GPA Calculator"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 4
challenge_type: "supplemental"   # regular | supplemental | discontinued
language: python
tags: [python]
author: "Your Name"
status: draft        # todo | draft | reviewed | final
---

# Supplemental Challenge #4: Type Casting and Numerical Operators - GPA Calculator

## Challenge Brief

https://lms.zebrarobotics.com/courses/2576/assignments/52711

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

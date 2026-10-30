---
title: "Challenge #53: Favorite Numbers Transformation"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 53
challenge_type: "regular"   # regular | supplemental | discontinued | optional | unnumbered
language: python
tags: [python]
author: "Your Name"
status: draft        # todo | draft | reviewed | final
---

# Challenge #53: Favorite Numbers Transformation

## Challenge Brief

https://lms.zebrarobotics.com/courses/2597/assignments/53236

## Solutions

```python
numbers = [3, 6, 9, 12, 15]

# Approach A - a lambda inside a list comprehension
transform = lambda n: n * 2 if n % 2 == 0 else n
resultA = [transform(n) for n in numbers]

# Approach B - a list comprehension with a conditional expression (no lambda)
resultB = [n * 2 if n % 2 == 0 else n for n in numbers]

print("Original:    " + str(numbers))
print("Approach A:  " + str(resultA))
print("Approach B:  " + str(resultB))
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

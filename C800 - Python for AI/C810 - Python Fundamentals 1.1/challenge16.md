---
title: "Challenge #16: Casting - Pizza Slices"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 16
challenge_type: "regular"   # regular | supplemental | discontinued
language: python
tags: [python]
author: "Your Name"
status: draft        # todo | draft | reviewed | final
---

# Challenge #16: Casting - Pizza Slices

## Challenge Brief

https://lms.zebrarobotics.com/courses/2576/assignments/52676

## Solutions

```python
totalSlices = int(input("How many pizza slices are there? "))
people = int(input("How many people are sharing? "))

each = totalSlices // people
leftOver = totalSlices % people

print("Each person gets " + str(each) + " slices.")
print("There are " + str(leftOver) + " slices left over.")
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

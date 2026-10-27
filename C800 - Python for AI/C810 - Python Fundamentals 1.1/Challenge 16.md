---
title: "Challenge #16: Casting - Pizza Slices"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 16
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #16: Casting - Pizza Slices

## Problem

Students keep arguing over how many pizza slices each of them should get.
They are not great at mental math, so they have asked you to help.

This time, the total number of pizza slices will be randomly generated using Python’s random module.

Task

Create a program that:

• Generates a random number of pizza slices (e.g., between 1 and 24).

• Asks the user how many students there are.

• Calculates:

• How many slices each student gets (rounded down)

• How many slices are left over

• Prints the results.

Hints

• Use import random

• To generate a random number between 1 and 24:

•
random.randint(1, 24)

• Use // (floor division) to divide slices equally.

• Use % (modulus) to find the leftover slices.

Example Output

There are 17 total pizza slices today!

How many students are here? 5

Each student gets 3 slice(s).

There will be 2 slice(s) left over.

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

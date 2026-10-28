---
title: "Challenge #53: Favorite Numbers Transformation"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 53
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #53: Favorite Numbers Transformation

## Problem

You and your friends have each chosen your favorite numbers. You want to double the even numbers and keep the odd numbers the same.

Instructions:

• Use a list to store your numbers: [3, 6, 9, 12, 15].

• Transform the list in two ways:

•
Approach A – Using a lambda expression inside a list comprehension

• Use a lambda to apply the transformation for each element.

•
Approach B – Using just a list comprehension with a conditional expression

• Apply the same transformation without a lambda.

• Print the original list and the transformed list.

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

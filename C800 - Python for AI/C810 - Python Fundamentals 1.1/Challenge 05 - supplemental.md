---
title: "Supplemental Challenge #05: String Manipulation - Username Creator"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 5
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "supplemental"
---

# Supplemental Challenge #05: String Manipulation - Username Creator

## Problem

Create a program that takes a user’s name, and their birth day, birth month, and birth year, then creates a user name like:

<name><birth day><birth month><birth year>

So if your name is: Odin

Birth day is: 31

Birth month is: 05

Birth year is: 2005

Odin’s user name should be: Odin31052005

## Solutions

```python
name = input("What is your name? ")
day = input("What day were you born? ")
month = input("What month were you born? ")
year = input("What year were you born? ")

username = name + day + month + year
print("Your user name is: " + username)
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

---
title: "Challenge #17: Strings - String Manipulation"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 17
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #17: Strings - String Manipulation

## Problem

Create a program that takes 2 strings of length 10 and prints out:

• The strings added together

• The strings repeated 3 times

• The strings converted to Uppercase AND added together

• The strings converted to Lowercase AND repeated 5 times

• The character at the 3rd index of each string

• Both the strings sliced from index 3 to index 9

## Solutions

```python
s1 = input("Enter the first string:")
s2 = input("Enter the second string:")

print("Added together: " + s1 + s2)
print("s1 repeated 3 times: " + s1 * 3)
print("s2 repeated 3 times: " + s2 * 3)
print("Uppercase and added together: " + s1.upper() + s2.upper())
print("s1 Lowercase and 5 times: " + s1.lower() * 5)
print("s2 Lowercase and 5 times: " + s2.lower() * 5)
print("s1 3rd letter: " + s1[2])
print("s2 3rd letter: " + s2[2])
print("s1 strings sliced 3-9: " + s1[3:9])
print("s2 strings sliced 3-9: " + s2[3:9])
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

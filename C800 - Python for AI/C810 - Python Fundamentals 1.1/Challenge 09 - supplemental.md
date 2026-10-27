---
title: "Supplemental Challenge #09: For Loops - Vowel Counter"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 9
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "supplemental"
---

# Supplemental Challenge #09: For Loops - Vowel Counter

## Problem

Create a program that takes input from a user and prints out the indexes of all the characters in the string. For example if given "Hello World", your output should look like:

H => 0

e => 1

l => 2

l => 3

o => 4

 => 5

W => 6

o => 7

r => 8

l => 9

d => 10

## Solutions

```python
text = input("Enter a string: ")

for i in range(len(text)):
    print(text[i] + " > " + str(i))
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

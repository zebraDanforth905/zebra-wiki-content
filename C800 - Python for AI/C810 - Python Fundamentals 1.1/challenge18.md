---
title: "Challenge #18: Strings - Username and Password"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 18
challenge_type: "regular"   # regular | supplemental | discontinued
language: python
tags: [python]
author: "Your Name"
status: draft        # todo | draft | reviewed | final
---

# Challenge #18: Strings - Username and Password

## Challenge Brief

https://lms.zebrarobotics.com/courses/2576/assignments/52678

## Solutions

```python
username = input("Enter a username: ")
password = input("Enter a password: ")

if username.isalpha() and len(password) >= 8:
    print("Account created!")
elif not username.isalpha():
    print("Your username must be all letters.")
else:
    print("Your password must be at least 8 characters long.")
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

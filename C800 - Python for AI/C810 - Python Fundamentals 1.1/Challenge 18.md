---
title: "Challenge #18: Strings - Username and Password"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 18
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #18: Strings - Username and Password

## Problem

Create a program that validates the username and password of the user.

• It should ask for input of the username and check that the username is all alphabetical--print true or false accordingly.

• It should also ask for the password of the user and check that the password is all digits--print true or false accordingly.

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

---
title: "Challenge #45: Functions - Greeter"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 45
challenge_type: "regular"   # regular | supplemental | discontinued
language: python
tags: [python]
author: "Your Name"
status: draft        # todo | draft | reviewed | final
---

# Challenge #45: Functions - Greeter

## Challenge Brief

https://lms.zebrarobotics.com/courses/2576/assignments/52705

## Solutions

```python
def greeter(name):
    print("Hello there, " + name + "!")
    print("It is so nice to see you, " + name + ".")
    print("Have a wonderful day, " + name + "!")


people = ["Alex", "Sam", "Jordan"]
for person in people:
    greeter(person)
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

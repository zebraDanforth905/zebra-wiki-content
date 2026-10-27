---
title: "Challenge #45: Functions - Greeter"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 45
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #45: Functions - Greeter

## Problem

• Write a function greeter(name) that takes in a person's name and prints out a greeting.

• The greeting must be at least three lines, and the person's name must be in each line.

• Use your function to greet at least three different people.

• Bonus: Store your three people in a list, and call your function from a for loop.

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

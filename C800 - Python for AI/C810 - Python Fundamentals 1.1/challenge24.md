---
title: "Challenge #24: Branching Logic  - Amusement Park"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 24
challenge_type: "regular"   # regular | supplemental | discontinued
language: python
tags: [python]
author: "Your Name"
status: draft        # todo | draft | reviewed | final
---

# Challenge #24: Branching Logic  - Amusement Park

## Challenge Brief

https://lms.zebrarobotics.com/courses/2576/assignments/52684

## Solutions

```python
height = int(input("How tall are you in inches? "))

print("You are allowed on these rides:")

if height >= 40:
    print("Tree Top Adventure, Taxi Jam, Sugar Shack")
if height >= 48:
    print("Vortex, Lumber Jack, Flying Canoes")
if height >= 54:
    print("Flight Deck, Behemoth, Leviathan")

if height < 40:
    print("Sorry, you are too short for any of the rides.")
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

---
title: "Challenge #24: Branching Logic  - Amusement Park"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 24
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #24: Branching Logic  - Amusement Park

## Problem

Extend challenge 23 to add the following rides and height restrictions; the program should print ALL rides the users are allowed to go on.

Ride and Height Requirement

Ride

Height

Vortex, Lumber Jack, Flying Canoes

48 inches

Flight Deck, Behemoth, Leviathan

54 inches

Tree Top Adventure, Taxi Jam, Sugar Shack

40 inches

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

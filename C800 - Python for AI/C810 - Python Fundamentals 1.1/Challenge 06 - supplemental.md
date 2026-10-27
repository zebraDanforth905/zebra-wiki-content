---
title: "Supplemental Challenge #06: Branching Logic - Horoscope Program"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 6
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "supplemental"
---

# Supplemental Challenge #06: Branching Logic - Horoscope Program

## Problem

Get the user's zodiac sign and give them a prediction based on the sign.

## Solutions

```python
sign = input("What is your zodiac sign? ")
sign = sign.lower()

if sign == "aries":
    print("A bold opportunity will come your way today.")
elif sign == "leo":
    print("Your confidence will help a friend today.")
elif sign == "scorpio":
    print("Trust your instincts on a tricky decision.")
elif sign == "pisces":
    print("A creative idea will make you smile.")
else:
    print("The stars say: today is full of possibilities!")
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

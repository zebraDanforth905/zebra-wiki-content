---
title: "Challenge #26: Random Money Action"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 26
challenge_type: "regular"   # regular | supplemental | discontinued
language: python
tags: [python]
author: "Your Name"
status: draft        # todo | draft | reviewed | final
---

# Challenge #26: Random Money Action

## Challenge Brief

https://lms.zebrarobotics.com/courses/2576/assignments/52686

## Solutions

```python
import random

money = int(input("How much money do you have? "))
action = random.randint(1, 5)

match action:
    case 1:
        money = money + 10
        print("You found $10! You now have $" + str(money))
    case 2:
        money = money - 5
        print("You lost $5! You now have $" + str(money))
    case 3:
        money = money * 2
        print("You doubled your money! You now have $" + str(money))
    case 4:
        money = 0
        print("You lost it all! You now have $" + str(money))
    case 5:
        print("Nothing happened. You still have $" + str(money))
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

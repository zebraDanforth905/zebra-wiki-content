---
title: "Challenge #48: Scope - Difference between global variable and local variable"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 48
challenge_type: "regular"   # regular | supplemental | discontinued | optional | unnumbered
language: python
tags: [python]
author: "Your Name"
status: draft        # todo | draft | reviewed | final
---

# Challenge #48: Scope - Difference between global variable and local variable

## Challenge Brief

https://lms.zebrarobotics.com/courses/2597/assignments/53230

## Solutions

```python
# Challenge 48: Explain the difference between a global and a local variable.
#
# A global variable is created outside of any function. It can be read from
# anywhere in the program.
#
# A local variable is created inside a function. It only exists while that
# function is running and cannot be used outside of it.

score = 0          # global variable

def play():
    bonus = 10     # local variable, only exists inside play()
    print("Bonus this round:", bonus)
    print("Total score so far:", score)

play()
print("Score is still global:", score)
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

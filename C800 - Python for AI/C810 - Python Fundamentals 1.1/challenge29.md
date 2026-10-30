---
title: "Challenge #29: Loops - Bottles of Milk"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 29
challenge_type: "regular"   # regular | supplemental | discontinued
language: python
tags: [python]
author: "Your Name"
status: draft        # todo | draft | reviewed | final
---

# Challenge #29: Loops - Bottles of Milk

## Challenge Brief

https://lms.zebrarobotics.com/courses/2576/assignments/52689

## Solutions

```python
bottles = 99

while bottles > 0:
    print(str(bottles) + " bottles of milk on the wall, " + str(bottles) + " bottles of milk.")
    print("Take one down and pass it around, " + str(bottles - 1) + " bottles of milk on the wall.")
    bottles = bottles - 1
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

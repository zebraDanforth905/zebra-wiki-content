---
title: "Challenge #52: List Comprehension - The Clean-Up Bot"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 52
challenge_type: "regular"   # regular | supplemental | discontinued | optional | unnumbered
language: python
tags: [python]
author: "Your Name"
status: draft        # todo | draft | reviewed | final
---

# Challenge #52: List Comprehension - The Clean-Up Bot

## Challenge Brief

https://lms.zebrarobotics.com/courses/2597/assignments/53235

## Solutions

```python
tasks = [
    "desk_cleaned", "floor_dirty", "window_cleaned",
    "chair_dirty", "board_cleaned", "door_dirty"
]

dirty = [task for task in tasks if "dirty" in task]
print(dirty)

cleaned = [task.replace("dirty", "cleaned") for task in dirty]
print(cleaned)
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

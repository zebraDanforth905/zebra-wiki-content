---
title: "Challenge #52: List Comprehension - The Clean-Up Bot"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 52
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #52: List Comprehension - The Clean-Up Bot

## Problem

A robot keeps a messy record of the items it’s supposed to clean:

tasks = [
    "desk_cleaned", "floor_dirty", "window_cleaned",
    "chair_dirty", "board_cleaned", "door_dirty"
]

Tasks:

• Use list comprehension to create a list of only the dirty items.

• Create another list that turns all “dirty” items into their cleaned version.
Example: "floor_dirty" → "floor_cleaned"

Expected Output:

['floor_dirty', 'chair_dirty', 'door_dirty']
['floor_cleaned', 'chair_cleaned', 'door_cleaned']

Bonus Challenge:
Do the same transformation using a dictionary comprehension,
where the key is the original item and the value is its cleaned version.

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

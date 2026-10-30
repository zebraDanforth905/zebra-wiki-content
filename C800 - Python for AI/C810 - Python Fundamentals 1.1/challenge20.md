---
title: "Challenge #20: Strings - Magical Story Validator"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 20
challenge_type: "regular"   # regular | supplemental | discontinued
language: python
tags: [python]
author: "Your Name"
status: draft        # todo | draft | reviewed | final
---

# Challenge #20: Strings - Magical Story Validator

## Challenge Brief

https://lms.zebrarobotics.com/courses/2576/assignments/52680

## Solutions

```python
story = input("Type your story: ")
story = story.lower()

startsRight = story.startswith("once upon a time") or story.startswith("long ago in a faraway land")
hasCreature = "dragon" in story or "unicorn" in story or "fairy" in story or "wizard" in story
endsRight = story.endswith("the end")

if startsRight and hasCreature and endsRight:
    print(True)
else:
    print(False)
    if not startsRight:
        print("It does not start the right way.")
    if not hasCreature:
        print("It is missing a magical creature.")
    if not endsRight:
        print("It does not end with THE END.")
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

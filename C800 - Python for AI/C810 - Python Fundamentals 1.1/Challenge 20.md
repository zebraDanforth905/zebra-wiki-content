---
title: "Challenge #20: Strings - Magical Story Validator"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 20
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #20: Strings - Magical Story Validator

## Problem

Create a program that checks if a story a person types is a “magical story.” A magical story must meet all three conditions:

• It starts with either "Once upon a time" or "Long ago in a faraway land" (ignore the case).

• It contains at least one magical creature, such as "dragon", "unicorn", "fairy", or "wizard" (ignore the case).

• It ends with "THE END" (ignore the case).

The program should:

• Take input from the user (the story).

• Check all three conditions in a case-insensitive way.

• Print True if all conditions are met, otherwise print False.

• Print which condition(s) failed if the story is not magical.

Example:

Input: once upon a time, a brave knight met a DRAGON. the end

Output: True

Input: Long ago in a faraway land, a princess danced in the castle.

Output: False (missing magical creature, missing THE END)

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

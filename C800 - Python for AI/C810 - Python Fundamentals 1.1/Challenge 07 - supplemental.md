---
title: "Supplemental Challenge #07: Lists - Riddler"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 7
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "supplemental"
---

# Supplemental Challenge #07: Lists - Riddler

## Problem

The time module in Python allows you to stop the program for a few seconds. For this challenge, we can use this module to build some suspense. To pause the program for a second, we can use the following code:

Here is another example; try it to see how the time module works:

Your challenge is to create a list of riddles, and then every time the program is run, show a user a random riddle and then show the answer after three seconds.

## Solutions

```python
import random
import time

riddles = [
    ["What has to be broken before you can use it?", "An egg"],
    ["I'm tall when I'm young and short when I'm old. What am I?", "A candle"],
    ["What has hands but cannot clap?", "A clock"],
    ["What has a head and a tail but no body?", "A coin"]
]

riddle = random.choice(riddles)
print(riddle[0])

time.sleep(3)

print("The answer is: " + riddle[1])
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

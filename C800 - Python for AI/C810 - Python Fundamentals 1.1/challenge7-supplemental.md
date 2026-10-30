---
title: "Supplemental Challenge #7: Lists - Riddler"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 7
challenge_type: "supplemental"   # regular | supplemental | discontinued
language: python
tags: [python]
author: "Your Name"
status: draft        # todo | draft | reviewed | final
---

# Supplemental Challenge #7: Lists - Riddler

## Challenge Brief

https://lms.zebrarobotics.com/courses/2576/assignments/52714

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

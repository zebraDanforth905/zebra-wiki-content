---
title: "Challenge #51: MDS - The Pixel Painter"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 51
challenge_type: "regular"   # regular | supplemental | discontinued | optional | unnumbered
language: python
tags: [python]
author: "Your Name"
status: draft        # todo | draft | reviewed | final
---

# Challenge #51: MDS - The Pixel Painter

## Challenge Brief

https://lms.zebrarobotics.com/courses/2597/assignments/53234

## Solutions

```python
import random

palette = ["red", "blue", "green", "yellow", "purple", "orange", "pink"]

canvas = [[random.choice(palette) for _ in range(3)] for _ in range(3)]
for row in canvas:
    print(row)

counts = {}
for row in canvas:
    for color in row:
        if color in counts:
            counts[color] = counts[color] + 1
        else:
            counts[color] = 1

print()
for color in counts:
    print(color + " -> " + str(counts[color]))
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

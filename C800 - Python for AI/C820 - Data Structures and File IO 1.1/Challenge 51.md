---
title: "Challenge #51: MDS - The Pixel Painter"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 51
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #51: MDS - The Pixel Painter

## Problem

Your job is to analyze a small digital painting, where each pixel has a color.
Instead of typing the colors manually, your program will generate them randomly from a palette!

The Setup

We have a list of seven colors:

import random

palette = ["red", "blue", "green", "yellow", "purple", "orange", "pink"]

Now we’ll randomly fill a 3x3 grid (list of lists) with colors:

canvas = [[random.choice(palette) for _ in range(3)] for _ in range(3)]

for row in canvas:
    print(row)

This prints something like:

['blue', 'green', 'red']
['red', 'yellow', 'pink']
['purple', 'blue', 'orange']

TASK: Count how many times each color appears in the grid.

For example:

red → 2
blue → 2
green → 1
yellow → 1
purple → 1
orange → 1
pink → 1

🪄 Hint: Use a dictionary to store colors as keys and their counts as values.
Each time you add a color to the grid, check if it’s already in the dictionary:

• If yes, increase its count by 1.

• If not, add it with a count of 1.

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

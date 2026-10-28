---
title: "Challenge #11: Fair Water Fountain Placement Simulation"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 11
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #11: Fair Water Fountain Placement Simulation

## Problem

A large outdoor fair is organized as a rectangular grid of R rows and C columns, where each cell represents a fair block with an expected crowd count.

• Each row represents a walking path through the fair.

• The city wants to install 2 water fountains in each row to maximize accessibility for visitors.

Best Fountain Location Definition:

For each block in a row:

• Consider the crowd count of:

• The current block

• The immediate left neighboring block

• The immediate right neighboring block

(For blocks on the edges, only available neighbors are included.)

Local Row Crowd Sum:

For every block:

Local Row Crowd Sum = Left Neighbor + Current Block + Right Neighbor
Objective:

For each row:

• Calculate the local row crowd sum for every block.

• Identify the top 2 blocks with the highest local row crowd sums.

• Output:

• Row number

• Column number

• Local row crowd sum

Goal:

By selecting the two highest-demand blocks in every row, water fountains will be placed where they can serve the largest concentration of nearby fair visitors.

Sample NumPy Grid:

import numpy as np

# Sample fair crowd expectation grid
fair_grid = np.array([
    [45, 60, 55, 70, 50, 65],
    [80, 75, 90, 85, 70, 60],
    [50, 65, 60, 75, 80, 55],
    [95, 85, 100, 90, 88, 76],
    [40, 55, 60, 58, 62, 50]
])

print("Fair Crowd Grid:")
print(fair_grid)

Your Task:

Part 1: Algorithm Design

Write the algorithm in clear English explaining how you would:

• Process each row

• Calculate local row crowd sums

• Determine the top 2 fountain locations per row

• Display the final results

Part 2: Pseudocode

Write pseudocode that:

• Iterates through each row

• Computes neighboring row sums

• Sorts or selects the top 2 values

• Outputs selected fountain positions

Part 3: Python Implementation

Using Python and NumPy:

• Represent the fair as a 2D NumPy array

• Calculate all row-based local crowd sums

• Determine the best 2 fountain positions for each row

• Display the selected positions and crowd sums clearly

Full Expected Output

Row 1:
Fountain 1 -> Column 3, Local Sum: 185
Fountain 2 -> Column 5, Local Sum: 185

Row 2:
Fountain 1 -> Column 3, Local Sum: 250
Fountain 2 -> Column 2, Local Sum: 245

Row 3:
Fountain 1 -> Column 4, Local Sum: 215
Fountain 2 -> Column 5, Local Sum: 210

Row 4:
Fountain 1 -> Column 2, Local Sum: 280
Fountain 2 -> Column 4, Local Sum: 278

Row 5:
Fountain 1 -> Column 4, Local Sum: 180
Fountain 2 -> Column 3, Local Sum: 173

## Solutions

```python
# Add solution(s) here
```

You can include multiple approaches in this section if needed.

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

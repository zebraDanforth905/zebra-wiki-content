---
title: "Challenge #15: Minimum Travel Cost in a City Grid"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 15
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #15: Minimum Travel Cost in a City Grid

## Problem

Scenario:
You are a delivery driver in a city represented as an R x C grid. Each cell in the grid contains the travel cost for that location.

• You start at the top-left corner (0, 0) and must reach the bottom-right corner (R-1, C-1).

• You can only move right or down at each step.

• Your goal is to minimize the total travel cost along the path.

Task:

• Write a Python program using DP to find the minimum total cost from the start to the destination.

• Input: A 2D list of integers representing travel costs.

• Output: The minimum total cost.

Example Input:

grid = [
    [1, 3, 1],
    [2, 1, 5],
    [4, 2, 1]
]

Expected Output:

Minimum travel cost: 7

Explanation:

• One optimal path: 1 → 3 → 1 → 1 → 1

• Total cost = 1 + 3 + 1 + 1 + 1 = 7

Hint:

• Use a two-dimensional (as the input is 2D) DP table where dp[i][j] stores the minimum cost to reach cell (i, j).

• Base case: dp[0][0] = grid[0][0]

• Transition: dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1]) (handle edges carefully).

## Solutions

```python
# Add solution(s) here
```

You can include multiple approaches in this section if needed.

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

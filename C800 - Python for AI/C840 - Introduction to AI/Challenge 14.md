---
title: "Challenge #14: Maximum Earnings from Daily Freelance Jobs"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 14
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #14: Maximum Earnings from Daily Freelance Jobs

## Problem

Scenario:
You are a freelancer who can accept one job per day for n days. Each day has a payment amount.

Rules:

• If you work on two consecutive days, you get tired and cannot take the next day’s job.

• You can choose to skip any day, but you cannot skip two consecutive days.

Your goal is to maximize your total earnings over the n days.

Task:

• Write a Python program that uses one-dimensional dynamic programming (1D DP) to compute the maximum total earnings over n days, where each day has a given payment, and you must follow specific constraints (rules) when choosing which days to work.

• Input: A list of integers representing daily payments.

• Output: Maximum earnings you can earn following the rules.

Example Input:

payments = [50, 10, 60, 20, 80]

Expected Output:

Maximum earnings: 190

Hint:

• Use a 1D DP array where each element represents the maximum earnings possible up to that day.

• Consider the choices of taking or skipping a day, making sure you follow the rules.

What does 1D DP mean here?

In dynamic programming (DP), we store solutions to smaller subproblems so we don’t recompute them again and again.

1D DP means:

• We use a single list (array) to store results.

• Each position in the list represents the best solution up to that point.

So instead of something complex like a 2D table (rows and columns), we only need:

dp[i]

Where:

dp[i] = maximum earnings we can achieve up to day i
Why is it called “1D”?

Because the DP structure looks like this:

Day:   0   1   2   3   4
dp:   [x,  x,  x,  x,  x]

Just one row → one dimension

## Solutions

```python
# Add solution(s) here
```

You can include multiple approaches in this section if needed.

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

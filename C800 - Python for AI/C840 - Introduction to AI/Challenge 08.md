---
title: "Challenge #08: Toronto Daily Temperatures"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 8
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #08: Toronto Daily Temperatures

## Problem

You are analyzing daily temperatures in Toronto over a period of five consecutive months to study seasonal trends.

Temperature Data Specifications

Each month has a different number of days and temperature range:

Month
Temperature Range (°C)
Number of Days

January
-5 to 2
31

February
-3 to 4
28

March
0 to 10
31

April
5 to 15
30

May
10 to 20
31

Part 1: Data Generation

Using NumPy, complete the following steps:

• Create a 5x31 2D NumPy array named temperatures where:

• Each row represents a month

• Each column represents a day

• Since each month has a different number of days:

• Use 31 columns (maximum month length) for consistency

• Fill unused positions with np.nan

•
Generate temperature values using NumPy’s random functions. To simulate realistic daily temperature data, use the NumPy random module:

• Use np.random.randint(low, high, size) to generate random integer temperatures

• Ensure values fall within the given temperature range for each month

• Example:

np.random.randint(-5, 3, size=31)

•

•

• This generates random temperatures from -5°C to 2°C for January

• Assign each generated array to the corresponding row in temperatures

• Replace extra unused day values (beyond the actual number of days in a month) with np.nan

Part 2: Data Analysis

Using NumPy functions, perform the following:

• Calculate the average temperature for each month
(Hint: Use functions that ignore NaN values, such as np.nanmean)

• Determine the highest temperature recorded across all months

• Determine the lowest temperature recorded across all months

• Identify all days where the temperature exceeded 15°C

• Find the month with the highest average temperature

• Find the month with the lowest average temperature

## Solutions

```python
# Add solution(s) here
```

You can include multiple approaches in this section if needed.

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

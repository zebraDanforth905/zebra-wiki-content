---
title: "Challenge #55: Toronto Rainfall Analyzer"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 55
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #55: Toronto Rainfall Analyzer

## Problem

Toronto Rainfall Analyzer

You have collected monthly average rainfall data for Toronto over the past 5 years. Each year has 12 months, and you want to analyze rainfall trends.

Data (mm):

rainfall_data = {
    "2019": [78, 64, 85, 92, 104, 112, 98, 105, 97, 83, 76, 88],
    "2020": [80, 60, 88, 95, 100, 110, 102, 108, 99, 85, 78, 90],
    "2021": [82, 66, 90, 97, 105, 115, 100, 110, 101, 87, 79, 92],
    "2022": [75, 62, 86, 93, 102, 108, 96, 103, 98, 84, 77, 89],
    "2023": [79, 65, 87, 94, 101, 113, 99, 107, 100, 86, 80, 91]
}

Instructions:

• For each year, calculate:

• Total annual rainfall

• Average monthly rainfall (mean)

• Median monthly rainfall

• Wettest month (max) and driest month (min)

• Create a new dictionary with each year as the key and its average rainfall as the value.

• Use a lambda expression to sort the years by average rainfall in descending order.

• Identify the wettest year and the driest year.

• Print a summary report showing all these statistics in a readable format.

Hints:

• Use sum(), max(), min() for totals and extremes.

• Use statistics.mean() and statistics.median() for average and median.

• You can combine dictionary comprehension with lambda sorting to order years by rainfall.

## Solutions

```python
rainfall_data = {
    "2019": [78, 64, 85, 92, 104, 112, 98, 105, 97, 83, 76, 88],
    "2020": [80, 60, 88, 95, 100, 110, 102, 108, 99, 85, 78, 90],
    "2021": [82, 66, 90, 97, 105, 115, 100, 110, 101, 87, 79, 92],
    "2022": [75, 62, 86, 93, 102, 108, 96, 103, 98, 84, 77, 89],
    "2023": [79, 65, 87, 94, 101, 113, 99, 107, 100, 86, 80, 91]
}

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

averages = {}

for year in rainfall_data:
    data = rainfall_data[year]
    total = sum(data)
    average = total / len(data)
    averages[year] = average

    ordered = sorted(data)
    middle = len(ordered) // 2
    median = ordered[middle]

    wettest = months[data.index(max(data))]
    driest = months[data.index(min(data))]

    print("Year " + year)
    print("  Total rainfall: " + str(total) + " mm")
    print("  Average month:  " + str(round(average, 1)) + " mm")
    print("  Median month:   " + str(median) + " mm")
    print("  Wettest month:  " + wettest + " (" + str(max(data)) + " mm)")
    print("  Driest month:   " + driest + " (" + str(min(data)) + " mm)")
    print()

# Sort the years by average rainfall, highest first, using a lambda
sortedYears = sorted(averages, key=lambda year: averages[year], reverse=True)
print("Years from wettest to driest (by average): " + str(sortedYears))
print("Wettest year: " + sortedYears[0])
print("Driest year: " + sortedYears[-1])
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

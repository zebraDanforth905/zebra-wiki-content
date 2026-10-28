---
title: "Challenge #17: Predictive Data Pattern - Toy Store Sales vs Advertising Hours"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 17
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #17: Predictive Data Pattern - Toy Store Sales vs Advertising Hours

## Problem

Scenario:
A toy store wants to predict weekly toy sales based on the number of hours spent on advertising.

Over 20 weeks, the store collected the following data:

Week
Advertising Hours
Toys Sold

1
1
50

2
2
52

3
1
49

4
3
55

5
2
53

6
4
60

7
3
57

8
5
65

9
4
62

10
6
70

11
5
68

12
7
75

13
6
72

14
8
78

15
7
74

16
9
82

17
8
80

18
10
85

19
9
83

20
11
90

The store wants to predict sales for future weeks based on planned advertising hours.

Your Task:

• Create NumPy arrays for advertising hours (x) and toys sold (y).

• Draw a scatter plot of the data to visualize the trend.

• Use linear regression to calculate the best-fit line.

• Plot the regression line on top of the scatter plot.

• Predict toy sales for:

• Week 21: 12 advertising hours

• Week 22: 10 advertising hours

• Display the graph with labels and title.

Hints:

• Use NumPy for arrays and regression:

m, b = np.polyfit(x, y, 1)
predicted = m*hours + b

## Solutions

```python
# Add solution(s) here
```

You can include multiple approaches in this section if needed.

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

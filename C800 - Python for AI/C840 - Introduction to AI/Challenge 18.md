---
title: "Challenge #18: Popular Generative AI Platforms"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 18
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #18: Popular Generative AI Platforms

## Problem

Scenario:
A tech education company surveyed 20 students to find out which Generative AI platform they use the most for creating images, writing code, or generating text. Students also rated how useful they find the platform on a scale of 1–10.

The platforms surveyed:

•
DALL·E – AI for images

•
ChatGPT – AI for text and coding

•
MidJourney – AI for artistic images

Sample Data (20 students):

Student
Platform
Usefulness Rating

1
ChatGPT
9

2
DALL·E
8

3
MidJourney
7

4
ChatGPT
10

5
DALL·E
7

6
MidJourney
9

7
ChatGPT
8

8
DALL·E
6

9
MidJourney
8

10
ChatGPT
9

11
ChatGPT
10

12
DALL·E
9

13
MidJourney
7

14
ChatGPT
8

15
DALL·E
7

16
MidJourney
6

17
ChatGPT
9

18
DALL·E
8

19
MidJourney
9

20
ChatGPT
10

Tasks:

• Create NumPy arrays for the platform choices and usefulness ratings.

•
Count how many students chose each platform and determine the most popular platform.

•
Calculate the average usefulness rating for each platform.

•
Visualize the results:

• Bar chart for the number of students per platform

• Bar chart for the average usefulness rating per platform

• Write a short interpretation:

• Which platform is most popular?

• Which platform has the highest average usefulness rating?

Hints:

• Use np.unique(platforms, return_counts=True) to count the platform preferences.

• Use boolean indexing for average usefulness per platform:

avg_chatgpt = np.mean(ratings[platforms == 'ChatGPT'])

• Use matplotlib.pyplot to create bar charts.

## Solutions

```python
# Add solution(s) here
```

You can include multiple approaches in this section if needed.

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

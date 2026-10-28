---
title: "Challenge #28: Fix Zara’s AI Drink Machine"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 28
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #28: Fix Zara’s AI Drink Machine

## Problem

At Zara’s Smart Café, a new AI-powered drink machine has been installed. The machine is supposed to automatically decide whether a drink is a Fresh Juice 🧃 or a Soda 🥤 based on its ingredients.

But there’s a problem…

Some customers are complaining that the machine is making mistakes! 😬
Zara calls you in as a data scientist to fix the system.

How the Machine Thinks

The machine only looks at two things:

•
Sugar Level (numeric) → how sweet the drink is

•
Drink Type (categorical) → "Juice" or "Soda"

From past data:

• Fresh juices have moderate sugar

• Sodas have higher sugar

Training Data

Sugar Levels (100 drinks)

sugar_levels = [8, 10, 12, 9, 11, 13, 14, 15, 16, 12,
9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
19, 20, 21, 22, 23, 24, 25, 26, 18, 19,
20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
30, 28, 26, 24, 22, 20, 18, 16, 14, 12,
11, 13, 15, 17, 19, 21, 23, 25, 27, 29]

Drink Type (100 drinks)

drink_type = [
"Juice","Juice","Juice","Juice","Juice","Juice","Juice","Juice","Juice","Juice",
"Juice","Juice","Juice","Juice","Juice","Juice","Juice","Juice","Juice","Juice",
"Soda","Soda","Soda","Soda","Soda","Soda","Soda","Soda","Soda","Soda",
"Soda","Soda","Soda","Soda","Soda","Soda","Soda","Soda","Soda","Soda",
"Juice","Juice","Juice","Juice","Juice","Juice","Juice","Juice","Juice","Juice",
"Soda","Soda","Soda","Soda","Soda","Soda","Soda","Soda","Soda","Soda",
"Juice","Juice","Juice","Juice","Juice","Juice","Juice","Juice","Juice","Juice",
"Soda","Soda","Soda","Soda","Soda","Soda","Soda","Soda","Soda","Soda",
"Soda","Soda","Soda","Soda","Soda","Soda","Juice","Juice","Juice","Juice",
"Juice","Juice","Juice","Soda","Soda","Soda","Soda","Soda","Soda","Soda"
]

Your Task

• Read the dataset containing sugar levels and drink types.

• Convert drink_type labels to numeric as 0/1 using list comprehension.

• Reshape the sugar level data into a NumPy feature arrays for the model.

• Create a K-Nearest Neighbors model using sugar_levels (x) and drink_type (y).

• Train the model using the dataset.

• Set the number of neighbors (k = 5).

• Input the three new drinks with sugar levels 16, 18, and 24 into the trained model.

• Use the model to predict the category of each new drink.

• Convert the predicted numeric labels back to "Juice" or "Soda".

## Solutions

```python
# Add solution(s) here
```

You can include multiple approaches in this section if needed.

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

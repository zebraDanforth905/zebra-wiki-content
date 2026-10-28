---
title: "Challenge #29: Sunny Lemonade Stand"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 29
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #29: Sunny Lemonade Stand

## Problem

At Sunny Lemonade Stand, the owner wants to predict how many glasses of lemonade will be sold based on the number of lemons available each day.

• More lemons → more lemonade → more sales.

• But sales aren’t perfectly predictable because customer demand and weather introduce small variations.

Your task is to train an AI regression model to learn this pattern and make predictions for new situations.

Training Data

# Input feature: lemons available each day
lemons = [7, 6, 8, 7, 10, 10, 10, 13, 13, 13,
          13, 13, 14, 14, 15, 17, 16, 18, 19, 19,
          20, 20, 22, 21, 22, 24, 25, 26, 27, 27,
          28, 28, 30, 30, 30, 31, 32, 34, 34, 34,
          35, 36, 36, 38, 39, 40, 40, 42, 43, 44]

# Target output: glasses of lemonade sold
sales = [9, 11, 12, 15, 18, 16, 20, 26, 27, 24,
         25, 25, 28, 31, 33, 33, 33, 37, 37, 37,
         40, 44, 43, 45, 47, 51, 53, 53, 55, 55,
         56, 58, 61, 60, 61, 64, 66, 68, 70, 70,
         71, 74, 73, 77, 78, 80, 82, 82, 84, 87]

Tasks to Complete

• Import necessary libraries (numpy and LinearRegression from sklearn.linear_model).

• Convert the lemons list into a 2D NumPy array suitable for training (reshape if needed).

• Convert the sales list into a NumPy array for the target variable.

• Create a Linear Regression model.

• Train the model using the provided training data.

• Predict the number of glasses sold for these new lemon counts:

• 18 lemons

• 29 lemons

• 36 lemons

• Print the predicted sales for each of the three new inputs.

• Round the predictions to one decimal place for clarity.

• (Optional) Visualize the training data and the regression line using a scatter plot and line plot.

## Solutions

```python
# Add solution(s) here
```

You can include multiple approaches in this section if needed.

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

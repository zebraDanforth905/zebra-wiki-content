---
title: "Challenge #30: Smart Vehicle Fuel Analyzer"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 30
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #30: Smart Vehicle Fuel Analyzer

## Problem

At Velocity Auto Lab, engineers are building an AI system to understand different types of vehicles based on how much fuel they consume.

But there’s a twist…

They don’t label vehicles as “economy,” “standard,” or “high consumption.” Instead, they only collect fuel consumption data (liters per 100 km).

Now, they need your help to build a system that can automatically group vehicles into categories based on fuel usage.

How the AI Should Think

• Each vehicle is a data point

• The only feature is fuel consumption (L/100 km)

• Vehicles with similar fuel usage should be grouped together

• The AI should discover patterns like:

• Fuel-efficient vehicles

• Moderate consumption vehicles

• High consumption vehicles

Dataset

fuel_consumption = [
4.7, 5.0, 5.3, 4.9, 5.2, 5.5, 5.1, 4.8, 5.4, 5.6,
6.0, 6.2, 6.5, 6.8, 6.1, 6.4, 6.7, 6.3, 6.6, 6.9,
7.2, 7.5, 7.8, 7.1, 7.4, 7.7, 7.3, 7.6, 7.9, 8.0,
8.3, 8.6, 8.9, 8.2, 8.5, 8.8, 8.1, 8.4, 8.7, 9.0,
9.3, 9.6, 9.9, 9.2, 9.5, 9.8, 9.1, 9.4, 9.7, 10.0,
10.5, 10.8, 11.0, 10.2, 10.6, 10.9, 10.3, 10.7, 11.2, 11.5,
12.0, 12.5, 13.0, 12.2, 12.8, 13.5, 12.3, 12.7, 13.2, 13.8,
14.0, 14.5, 15.0, 14.2, 14.8
]

Tasks to Complete

• Import the required libraries (numpy, KMeans from sklearn.cluster)

• Convert the dataset into a NumPy array

• Reshape the data into a 2D format

• Create a K-Means model with 3 clusters

• Train the model using the dataset

• Assign each vehicle to a cluster

• Extract the cluster centroids

• Print all centroid values

• Sort the centroids and interpret each group (low, medium, high fuel consumption)

• Predict which cluster a new vehicle with fuel consumption 9.3 L/100 km belongs to

## Solutions

```python
# Add solution(s) here
```

You can include multiple approaches in this section if needed.

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

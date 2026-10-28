---
title: "Challenge #20: Sentiment Analysis and Word Clouds"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 20
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #20: Sentiment Analysis and Word Clouds

## Problem

Scenario:

You are a data analyst for a company that collects customer reviews. You have a dataset of 1000 customer reviews, where each review includes:

•
Rating (1–10)

•
Comment (a detailed text describing the experience)

Your goal is to explore the patterns in the text of positive and negative reviews using Python.

Tasks:

Step 1: Load and Explore Data

• Open the CSV file customer_reviews_1000_detailed.csv using open() and readlines().

• Skip the header row and split each line into rating and comment.

• Store ratings and comments in NumPy arrays for easy processing.

• Check the first few entries to understand the structure of the data.

Step 2: Categorize Reviews (Initial Sentiment)

•
Positive reviews: Ratings > 5

•
Negative reviews: Ratings ≤ 5

• Use NumPy boolean masks to separate comments based on these conditions.

Step 3: Text Processing

• Convert all text to lowercase.

•
Remove punctuation from each comment using str.translate().

• Remove common stopwords (e.g., “the”, “and”, “is”) using NLTK’s stopword list.

• Split comments into lists of words for analysis.

Step 4: Visualize Word Patterns

• Generate two word clouds:

• One for positive reviews

• One for negative reviews

• Use WordCloud and matplotlib.pyplot to display the patterns.

Step 5: Refined Sentiment Analysis

• Introduce a buffer zone to focus on clearly happy or unhappy customers:

•
Positive: Rating ≥ 7

•
Negative: Rating ≤ 4

• Ignore ratings 5 and 6.

• Repeat text processing (Step 3) and word cloud visualization (Step 4) for these refined categories.

Step 6: Analyze Frequent Words

• Count the most frequent words in:

• Positive (happy) comments

• Negative (angry/dissatisfied) comments

• Use collections.Counter to identify the top 10 words in each group.

• Compare word usage between happy and unhappy customers to understand sentiment patterns

## Solutions

```python
# Add solution(s) here
```

You can include multiple approaches in this section if needed.

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

- https://dp4rp4tcpuoo1.cloudfront.net/C800/Introduction%20to%20AI/Class%206/customer_reviews_1000_detailed.csv

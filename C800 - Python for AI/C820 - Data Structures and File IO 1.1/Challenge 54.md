---
title: "Challenge #54: School Timetable Analyzer"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 54
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #54: School Timetable Analyzer

## Problem

You are analyzing your school timetable for the week. Each day has multiple periods, and each period has a subject. You want to count how many times each subject occurs in a week.

Instructions:

• Represent the timetable as a list of lists (7 days × variable periods per day). Example:

timetable = [
    ["Math", "English", "Physics", "Art"],
    ["Biology", "Math", "English", "Music"],
    ["Math", "History", "English", "PE"],
    ["Math", "English", "Chemistry", "Art"],
    ["Physics", "Math", "English", "Music"],
    ["Biology", "Math", "English", "Drama"],
    ["Math", "English", "History", "PE"]
]

• Use a dictionary to count how many times each subject appears in the week.

• Identify most frequent subject(s) and least frequent subject(s).

• Print a summary report with:

• Each subject and its total count

• The most frequent subject

• The least frequent subject

Hints:

• Loop through days and then periods to update the dictionary.

• Use max() and min() with key=dictionary.get to find most/least frequent subjects.

NOTE:  Using max() and min() with key=books_read.get

When you have a dictionary where the keys are items (friends’ names) and the values are counts (books read), you can find the friend who read the most or least books.

Example Dictionary

books_read = {
    "Alice": 12,
    "Bob": 8,
    "Charlie": 15,
    "Diana": 10
}

Goal

• Find the friend who read the most books → Charlie

• Find the friend who read the least books → Bob

How max() works

Normally, max(dictionary) returns the largest key alphabetically:

print(max(books_read))  # Output: 'Diana' (alphabetical max)

This is not what we want. We want the key with the largest value.

Solution: key=books_read.get

most_books = max(books_read, key=books_read.get)
least_books = min(books_read, key=books_read.get)

Step-by-step explanation using books_read.get(key):

•
books_read.get(key) returns the value associated with a key (number of books read).

•
max(books_read, key=books_read.get) works like this internally:

# Pseudo-step-by-step
for key in books_read:
    value = books_read.get(key)   # Get the number of books
# Compare values and pick the key with the largest value

•
min(books_read, key=books_read.get) works similarly for the smallest value.

## Solutions

```python
timetable = [
    ["Math", "English", "Physics", "Art"],
    ["Biology", "Math", "English", "Music"],
    ["Math", "History", "English", "PE"],
    ["Math", "English", "Chemistry", "Drama"],
    ["Math", "English", "History", "PE"]
]

counts = {}
for day in timetable:
    for subject in day:
        if subject in counts:
            counts[subject] = counts[subject] + 1
        else:
            counts[subject] = 1

print("Subject counts for the week:")
for subject in counts:
    print(subject + ": " + str(counts[subject]))

mostFrequent = max(counts, key=counts.get)
leastFrequent = min(counts, key=counts.get)

print("\nMost frequent subject: " + mostFrequent)
print("Least frequent subject: " + leastFrequent)
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

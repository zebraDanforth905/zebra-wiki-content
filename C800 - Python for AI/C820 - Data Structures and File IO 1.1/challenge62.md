---
title: "Challenge #62: Parsing Files - Creating a suggestions file for a banking app"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 62
challenge_type: "regular"   # regular | supplemental | discontinued | optional | unnumbered
language: python
tags: [python]
author: "Your Name"
status: draft        # todo | draft | reviewed | final
---

# Challenge #62: Parsing Files - Creating a suggestions file for a banking app

## Challenge Brief

https://lms.zebrarobotics.com/courses/2597/assignments/53245

## Solutions

```python
keywords = ["Password", "Security", "E-transfer", "accounts", "cards", "Deposit", "branch"]

fileObj = open("suggestions.txt", "r")
text = fileObj.read().lower()
fileObj.close()

# split the file into words and strip punctuation off each one
words = []
for word in text.split():
    cleaned = ""
    for letter in word:
        if letter.isalpha() or letter == "-":
            cleaned = cleaned + letter
    words.append(cleaned)

counts = {}
for keyword in keywords:
    counts[keyword] = 0

# count without using .count()
for word in words:
    for keyword in keywords:
        if word == keyword.lower():
            counts[keyword] = counts[keyword] + 1

print("Suggestion keyword counts:")
for keyword in keywords:
    print(keyword + ": " + str(counts[keyword]))
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

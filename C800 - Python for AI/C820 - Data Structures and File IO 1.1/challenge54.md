---
title: "Challenge #54: School Timetable Analyzer"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 54
challenge_type: "regular"   # regular | supplemental | discontinued | optional | unnumbered
language: python
tags: [python]
author: "Your Name"
status: draft        # todo | draft | reviewed | final
---

# Challenge #54: School Timetable Analyzer

## Challenge Brief

https://lms.zebrarobotics.com/courses/2597/assignments/53237

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

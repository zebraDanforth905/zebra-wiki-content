---
title: "Challenge #61: Parsing Files - Make a list of students"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 61
challenge_type: "regular"   # regular | supplemental | discontinued | optional | unnumbered
language: python
tags: [python]
author: "Your Name"
status: draft        # todo | draft | reviewed | final
---

# Challenge #61: Parsing Files - Make a list of students

## Challenge Brief

https://lms.zebrarobotics.com/courses/2597/assignments/53244

## Solutions

```python
fileObj = open("student_marks.txt", "r")
lines = fileObj.readlines()
fileObj.close()

results = []
for line in lines:
    parts = line.split()
    name = parts[0].replace("-", " ")
    marks = []
    for mark in parts[1:]:
        marks.append(int(mark))

    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)
    lowest = min(marks)

    results.append({
        "name": name,
        "total": total,
        "average": average,
        "highest": highest,
        "lowest": lowest
    })

outObj = open("student_summary.txt", "w")
for student in results:
    line = (student["name"] +
            " | Total: " + str(student["total"]) +
            " | Average: " + str(round(student["average"], 1)) +
            " | Highest: " + str(student["highest"]) +
            " | Lowest: " + str(student["lowest"]))
    print(line)
    outObj.write(line + "\n")
outObj.close()

print("\nSummary written to student_summary.txt")
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

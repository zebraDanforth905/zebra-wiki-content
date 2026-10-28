---
title: "Challenge #61: Parsing Files - Make a list of students"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 61
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #61: Parsing Files - Make a list of students

## Problem

You are given a text file called student_marks.txt that contains students’ names and their marks for five tests in a given subject. Each mark is out of 20 points.

The data is stored in the following format, with values separated by spaces:

FirstName-LastName Marks1 Marks2 Marks3 Marks4 Marks5

Sample File (student_marks.txt)

Alice-Wong 18 17 19 20 16
Brandon-Lee 12 15 14 13 15
Chloe-Smith 20 20 19 19 20
Daniel-Jones 10 12 8 9 11
Ella-Martin 16 15 17 18 15
Felix-Ramirez 19 18 20 19 19
Grace-Liu 14 13 15 12 14
Hassan-Patel 17 19 16 18 17

Your Tasks:

•
Read the data from the file and store it in a suitable data structure (list or dictionary).
Hint: You may use .index() and/or .split() to separate data points.

•
Calculate the following for each student:

•
Total marks (sum of all 5 test scores)

•
Average mark

•
Highest mark

•
Lowest mark

•
Store the results in a new data structure, such as a list of dictionaries.

•
Write the processed results into a new file called student_summary.txt, formatted like this:

FirstName LastName | Total: XX | Average: XX.X | Highest: XX | Lowest: XX

Example Output:

Alice Wong | Total: 90 | Average: 18.0 | Highest: 20 | Lowest: 16
Brandon Lee | Total: 69 | Average: 13.8 | Highest: 15 | Lowest: 12

•
Final Steps:
After processing all students, display:

•

• The top-performing student (highest total score)

• The class average (average of all students’ averages)

• The test number where students performed best overall (highest average among the five tests)

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

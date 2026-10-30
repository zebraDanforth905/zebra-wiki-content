---
title: "Challenge #40: Organize a Classroom Database with Tuples, Sets, and Lists"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 40
challenge_type: "regular"   # regular | supplemental | discontinued
language: python
tags: [python]
author: "Your Name"
status: draft        # todo | draft | reviewed | final
---

# Challenge #40: Organize a Classroom Database with Tuples, Sets, and Lists

## Challenge Brief

https://lms.zebrarobotics.com/courses/2576/assignments/52700

## Solutions

```python
# Each student ID maps to:
#   a tuple for the birthdate (year, month, day) -> never changes
#   a set for the subjects taken -> no duplicates
#   a list for the books read -> order matters and duplicates are allowed
classroom = {
    "S001": {
        "birthdate": ("2005", "08", "15"),
        "subjects": {"Math", "Science"},
        "books": ["Holes", "Hatchet", "Holes"]
    },
    "S002": {
        "birthdate": ("2006", "01", "30"),
        "subjects": {"English", "Art", "Math"},
        "books": ["Wonder", "Matilda"]
    }
}

for studentId in classroom:
    student = classroom[studentId]
    print("ID: " + studentId +
          ", Birthdate: " + str(student["birthdate"]) +
          ", Subjects: " + str(student["subjects"]) +
          ", Books Read: " + str(student["books"]))
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

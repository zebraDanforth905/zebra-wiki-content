---
title: "Challenge #40: Organize a Classroom Database with Tuples, Sets, and Lists"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 40
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #40: Organize a Classroom Database with Tuples, Sets, and Lists

## Problem

You are asked to create a simple database for a classroom. The data you need to store is:

•
Student Names → each student has a unique ID.

•
Subjects Taken by Each Student → each student can take multiple subjects, but no duplicates.

•
Birthdates of Each Student → stored as components: year, month, day; birthdates are immutable once entered.

•
Books Read by Each Student → a student can read multiple books, including repeated books, in order of reading.

Task

• Create a dictionary where:

• Keys are student IDs.

• Values are a combination of tuples, sets, and lists, depending on the type of data.

• Decide which data structure fits each type of data:

•
Tuple → immutable data (birthdate components).

•
Set → unique items (subjects).

•
List → ordered data, possibly with duplicates (books read).

• Print out the dictionary in a readable format.

Example Output:

ID: S001, Birthdate: ('2005', '08', '15'), Subjects: {'Math', 'Science'}, Books Read: ['Harry Potter', '1984', 'Harry Potter']
ID: S002, Birthdate: ('2006', '03', '22'), Subjects: {'Math', 'English', 'Art'}, Books Read: ['The Hobbit', '1984']
ID: S003, Birthdate: ('2005', '12', '10'), Subjects: {'History', 'Science'}, Books Read: ['Harry Potter', 'The Hobbit', 'The Hobbit']

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

---
title: "Challenge #56: Reading Files - Create a text file with questions and answers"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 56
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #56: Reading Files - Create a text file with questions and answers

## Problem

Create a text file with 3 (or more) questions and answers like so:

Then create a program that reads in the questions and answers and quizzes a user and gives them a grade at the end.

Sample input:

## Solutions

```python
fileObj = open("questions.txt", "r")
lines = fileObj.readlines()
fileObj.close()

score = 0
for line in lines:
    line = line.strip()
    question = line[:line.index(":")]
    answer = line[line.index(":") + 1:]

    guess = input(question + " ")
    if guess.lower() == answer.lower():
        print("Correct!")
        score = score + 1
    else:
        print("Wrong. The answer was " + answer + ".")

print("You scored " + str(score) + " out of " + str(len(lines)) + ".")
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

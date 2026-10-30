---
title: "Challenge #56: Reading Files - Create a text file with questions and answers"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 56
challenge_type: "regular"   # regular | supplemental | discontinued | optional | unnumbered
language: python
tags: [python]
author: "Your Name"
status: draft        # todo | draft | reviewed | final
---

# Challenge #56: Reading Files - Create a text file with questions and answers

## Challenge Brief

https://lms.zebrarobotics.com/courses/2597/assignments/53239

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

---
title: "Challenge #32: For Loops - Sentence Splitter"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 32
challenge_type: "regular"   # regular | supplemental | discontinued
language: python
tags: [python]
author: "Your Name"
status: draft        # todo | draft | reviewed | final
---

# Challenge #32: For Loops - Sentence Splitter

## Challenge Brief

https://lms.zebrarobotics.com/courses/2576/assignments/52692

## Solutions

```python
word = input("Please enter a word: ")

result = ""
for letter in word:
    result = result + letter + "-"

# remove the extra dash on the end
print(result[:-1])
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

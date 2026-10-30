---
title: "Challenge #30: Loops - Remove Vowels"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 30
challenge_type: "regular"   # regular | supplemental | discontinued
language: python
tags: [python]
author: "Your Name"
status: draft        # todo | draft | reviewed | final
---

# Challenge #30: Loops - Remove Vowels

## Challenge Brief

https://lms.zebrarobotics.com/courses/2576/assignments/52690

## Solutions

```python
sentence = input("Enter a sentence: ")

result = ""
i = 0
while i < len(sentence):
    if sentence[i] not in "aeiou":
        result = result + sentence[i]
    i = i + 1

print(result)
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

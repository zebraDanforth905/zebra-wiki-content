---
title: "Supplemental Challenge #10: For Loops - Index Of Improved"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 10
challenge_type: "supplemental"   # regular | supplemental | discontinued
language: python
tags: [python]
author: "Your Name"
status: draft        # todo | draft | reviewed | final
---

# Supplemental Challenge #10: For Loops - Index Of Improved

## Challenge Brief

https://lms.zebrarobotics.com/courses/2576/assignments/52717

## Solutions

```python
text = input("Enter a string: ")
character = input("Which character do you want the index of? ")

if text == "":
    print(-1)
elif character not in text:
    print(-1)
else:
    indexes = []
    for i in range(len(text)):
        if text[i] == character:
            indexes.append(i)
    print(indexes)
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

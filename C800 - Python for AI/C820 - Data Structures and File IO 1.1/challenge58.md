---
title: "Challenge #58: Reading/Writing Files -Reconstructing a Passage from Two Files"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 58
challenge_type: "regular"   # regular | supplemental | discontinued | optional | unnumbered
language: python
tags: [python]
author: "Your Name"
status: draft        # todo | draft | reviewed | final
---

# Challenge #58: Reading/Writing Files -Reconstructing a Passage from Two Files

## Challenge Brief

https://lms.zebrarobotics.com/courses/2597/assignments/53241

## Solutions

```python
oddObj = open("oddWords.txt", "r")
oddWords = oddObj.read().split()
oddObj.close()

evenObj = open("evenWords.txt", "r")
evenWords = evenObj.read().split()
evenObj.close()

passage = []
for i in range(len(oddWords)):
    passage.append(oddWords[i])
    if i < len(evenWords):
        passage.append(evenWords[i])

outObj = open("reconstructed_passage.txt", "w")
for word in passage:
    outObj.write(word + "\n")
outObj.close()

print(" ".join(passage))
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

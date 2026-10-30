---
title: "Optional Challenge: Parsing Files -Figure out the encrypted message"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: null
challenge_type: "optional"   # regular | supplemental | discontinued | optional | unnumbered
language: python
tags: [python]
author: "Your Name"
status: draft        # todo | draft | reviewed | final
---

# Optional Challenge: Parsing Files -Figure out the encrypted message

## Challenge Brief

https://lms.zebrarobotics.com/courses/2597/assignments/53259

## Solutions

```python
# The first line of the file is the shift value. Every letter after that has
# been shifted forward by that amount, so we shift each letter back to decode.

fileObj = open("encrypted_message.txt", "r")
lines = fileObj.readlines()
fileObj.close()

shift = int(lines[0].strip())
encrypted = lines[1].rstrip("\n")

message = ""
for letter in encrypted:
    if letter.isalpha():
        message = message + chr((ord(letter) - ord("a") - shift) % 26 + ord("a"))
    else:
        message = message + letter

print(message)
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

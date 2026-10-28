---
title: "Challenge #57: Reading Files - Create a program that reads a corrupted file"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 57
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #57: Reading Files - Create a program that reads a corrupted file

## Problem

Your job is to create a program that reads an corrupted file and spits out only odd letters to decrypt the file.

Here is an example of an encrypted file:

Here is the message hidden in the odd letters:

## Solutions

```python
fileObj = open("corrupted.txt", "r")
text = fileObj.read().strip()
fileObj.close()

# The real message is hidden in the odd-numbered letters
# (the 1st, 3rd, 5th... characters), which are the even indexes.
message = text[::2]
print(message)
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

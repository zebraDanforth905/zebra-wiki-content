---
title: "Challenge #59: Writing Files - Write a program to encrypt files"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 59
challenge_type: "regular"   # regular | supplemental | discontinued | optional | unnumbered
language: python
tags: [python]
author: "Your Name"
status: draft        # todo | draft | reviewed | final
---

# Challenge #59: Writing Files - Write a program to encrypt files

## Challenge Brief

https://lms.zebrarobotics.com/courses/2597/assignments/53242

## Solutions

```python
# Caesar Cipher file encryptor. Reads a file, shifts every letter by a key,
# and writes the encrypted version to a new file.

shift = int(input("How many letters do you want to shift by (1-25)? "))

fileObj = open("secret.txt", "r")
text = fileObj.read()
fileObj.close()

encrypted = ""
for letter in text:
    if letter.isalpha():
        if letter.islower():
            start = ord("a")
        else:
            start = ord("A")
        encrypted = encrypted + chr((ord(letter) - start + shift) % 26 + start)
    else:
        encrypted = encrypted + letter

outObj = open("secret_encrypted.txt", "w")
outObj.write(encrypted)
outObj.close()

print("Encrypted file saved as secret_encrypted.txt")
print(encrypted)
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

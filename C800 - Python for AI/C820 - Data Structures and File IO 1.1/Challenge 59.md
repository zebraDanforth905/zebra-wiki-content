---
title: "Challenge #59: Writing Files - Write a program to encrypt files"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 59
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #59: Writing Files - Write a program to encrypt files

## Problem

You are asked to create a program that can encrypt text files. Students can choose one of the following encryption methods:

Caesar Cipher (Simple Shift Cipher)

•
Concept: Shift each letter in the text by a fixed number of positions in the alphabet.

•
Example: With a shift of 3:

A → D, B → E, C → F

Vigenère Cipher (Shifting by a Keyword)

•
Concept: Use a keyword to determine the shift for each letter. Each letter of the keyword corresponds to a shift for the text letter at the same position.

•
Example:

Text:    H  E  L  L  O
Keyword: K  E  Y  K  E

Calculation:

H (7) + K (10) = 17 → R
E (4) + E (4)  = 8  → I
L (11) + Y (24) = 35 → 35 % 26 = 9 → J
L (11) + K (10) = 21 → V
O (14) + E (4) = 18 → S

•
Encrypted Text: RIJVS

Substitution Cipher (Using a Substitute Alphabet)

•
Concept: Replace each letter in the text with a different letter or symbol according to a mapping.

•
Example:

Original alphabet:    ABCDEFGHIJKLMNOPQRSTUVWXYZ
Substitute alphabet:  QWERTYUIOPASDFGHJKLZXCVBNM
Text: HELLO → ITSSG

Google these ciphers if you need more details.

Challenge Instructions:

• Ask the user for:

•
Input file name (text file to encrypt)

•
Output file name (file to save encrypted text)

•
Encryption method (Caesar, Vigenère, or Substitution)

• If Caesar Cipher: Ask for shift number.

• If Vigenère Cipher: Ask for keyword.

• If Substitution Cipher: Either generate a random mapping or let the user provide one.

• Encrypt the content of the input file using the chosen method:

• For Caesar and Vigenère, only letters are encrypted; punctuation and spaces remain unchanged.

• Substitution replaces letters according to the mapping.

• Write the encrypted content to the output file.

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

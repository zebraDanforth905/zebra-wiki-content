---
title: "Challenge #58: Reading/Writing Files -Reconstructing a Passage from Two Files"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 58
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #58: Reading/Writing Files -Reconstructing a Passage from Two Files

## Problem

Reconstructing a Passage from Two Files

You are given two text files, each containing words from a passage. The original passage has been split so that:

•
oddWords.txt → words at odd positions

•
evenWords.txt → words at even positions

Your task is to reconstruct the original passage by interleaving the words correctly and saving the output to a new file.

Input Files

oddWords.txt

Python a general-purpose language Its philosophy code readability the significant Python dynamically and supports multiple structured particularly object-oriented functional

evenWords.txt

is high-level, programming. design emphasizes with use of indentation. is type-checked garbage-collected. It programming paradigms, including procedural), and programming.

Goal:

• Read the words from both files into separate lists.

• Interleave the words: take one word from oddWords, then one from evenWords, repeat…

• Write the combined words to a new file called reconstructed_passage.txt, one word per line.

• Optionally, print the full reconstructed passage on one line using ' '.join(words).

Expected output (single line):

Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically type-checked and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming.

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

---
title: "Challenge #30: Loops - Remove Vowels"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 30
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #30: Loops - Remove Vowels

## Problem

Write a Python program that:

• Prompts the user to enter a sentence.

• Uses a while loop to remove all vowels (a, e, i, o, u) from the sentence.

• Prints the resulting sentence back to the screen.

Example

Input:

Enter a sentence: Hello, how are you?

Output:

Hll, hw r y?

Hints

• Use a counter variable to keep track of the current character index.

• Use the while loop to iterate through each character in the sentence.

• Add characters that are not vowels to a new string.

• Remember to handle uppercase and lowercase vowels.

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

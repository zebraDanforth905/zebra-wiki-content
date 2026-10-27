---
title: "Supplemental Challenge #10: For Loops - Index Of Improved"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 10
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "supplemental"
---

# Supplemental Challenge #10: For Loops - Index Of Improved

## Problem

Ask the user for a string . Then ask them for a character they want the index of:

• If the string is empty, return a -1

• If the string doesn’t contain the character they asked for, return a -1

• If the character exists

• Find all the occurrences of the character and add the indexes to a list

For example:

Hello World would return:

For character ‘x’ => -1

For character ‘e’ => [1]

For character ‘o’ => [4, 7]

For character ‘l’ => [2,3,9]

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

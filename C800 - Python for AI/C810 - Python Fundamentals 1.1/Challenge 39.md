---
title: "Challenge #39: Dictionaries - Animal Names"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 39
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #39: Dictionaries - Animal Names

## Problem

Create a dictionary of animals and the name of their babies as Key-Value pair. Use the list below for guidance, or you can add your own. The users should be able to check what an animal’s babies are called. If the list does not have the animal a user enters, tell the user that the animal is not on the list.

List of animals and their babies:
hippo -> calf
horse -> foal
dog -> pup
kangaroo -> joey
monkey -> infant
owl -> owlet
parrot -> chick
rabbit -> bunny
rat -> pup
cow -> calf
skunk -> kit
sheep -> lamb

## Solutions

```python
animals = {
    "dog": "puppy",
    "cat": "kitten",
    "cow": "calf",
    "horse": "foal",
    "kangaroo": "joey"
}

for animal in animals:
    print("A baby " + animal + " is called a " + animals[animal] + ".")
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

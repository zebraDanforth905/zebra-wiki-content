---
title: "Challenge #36: For Loops - Stick Man"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 36
challenge_type: "regular"   # regular | supplemental | discontinued
language: python
tags: [python]
author: "Your Name"
status: draft        # todo | draft | reviewed | final
---

# Challenge #36: For Loops - Stick Man

## Challenge Brief

https://lms.zebrarobotics.com/courses/2576/assignments/52696

## Solutions

```python
import random

words = ["python", "turtle", "dragon", "guitar", "planet",
         "rocket", "garden", "pencil", "wizard", "yellow"]

word = random.choice(words)
print("The word has " + str(len(word)) + " letters.")

for attempt in range(5):
    letter = input("Guess a letter: ")
    if letter in word:
        print("Yes! '" + letter + "' is in the word.")
    else:
        print("Sorry, '" + letter + "' is not in the word.")

finalGuess = input("Now guess the whole word: ")
if finalGuess == word:
    print("You win! The word was " + word + ".")
else:
    print("You lose! The word was " + word + ".")
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

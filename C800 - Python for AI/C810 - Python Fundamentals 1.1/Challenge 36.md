---
title: "Challenge #36: For Loops - Stick Man"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 36
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #36: For Loops - Stick Man

## Problem

We are going to create a Stick Man like program. Make sure you test every step properly before you move on to the next one.

• Make a list to store 10 words.

• Pick a random word from the list and save it somewhere.

• Print the length of the random word.

• Give players 5 chances to guess the letters in the word while giving them appropriate success and failure messages.

• Hint: you can use if i in word - to check if a particular letter is in the word.

• On the 6th attempt, ask them to guess the whole word. Compare the randomly selected words with the user’s guess; if it is correct, the user wins.

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

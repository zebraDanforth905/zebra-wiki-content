---
title: "Challenge #41: Dictionaries - Animal Menu"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 41
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #41: Dictionaries - Animal Menu

## Problem

We will add onto the code from Challenges 26 and 27. Create a Menu for the user to select as seen below:

For a explanation of how to add a menu to your video, watch the following video:

Note: You can also effectively use a "match" statement to manage the actions based on a menu.

## Solutions

```python
animals = {
    "dog": "puppy",
    "cat": "kitten",
    "cow": "calf",
    "horse": "foal",
    "kangaroo": "joey"
}

option = 0
while option != 4:
    print("\n1) See all animals")
    print("2) Look up a baby animal's name")
    print("3) Add a new animal")
    print("4) Exit")
    option = int(input("Choose an option: "))

    match option:
        case 1:
            for animal in animals:
                print(animal + " -> " + animals[animal])
        case 2:
            animal = input("Which animal? ")
            if animal in animals:
                print("A baby " + animal + " is called a " + animals[animal] + ".")
            else:
                print("That animal is not in the dictionary.")
        case 3:
            animal = input("Animal name: ")
            baby = input("Baby name: ")
            animals[animal] = baby
            print("Added!")
        case 4:
            print("Goodbye!")
        case _:
            print("Invalid option!")
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

- https://iframe.mediadelivery.net/embed/711340/bfdd9631-283d-4faf-bcfe-83da2ffc5d28?autoplay=false&preload=false

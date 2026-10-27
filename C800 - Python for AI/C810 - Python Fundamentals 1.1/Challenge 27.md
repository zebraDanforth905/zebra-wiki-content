---
title: "Challenge #27: Lists - Travel Wishlist"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 27
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #27: Lists - Travel Wishlist

## Problem

Create a program that displays the following menu for a user to manage their travel destination wish list:

• Add a travel destination

• Find a travel destination

• Remove a travel destination

• Sort destinations by alphabet

• Count destinations

If the user enters 1, you will ask them which travel destination they want to add and add it to a list of destinations, and then print the list of destinations.

If a user enters 2, ask them which destination they want to find, if it is in the list print the index of the destination. Do as the description states for all other menu items.

You can have a default list to begin.

## Solutions

```python
destinations = ["Japan", "Italy", "Brazil"]

option = 0
while option != 6:
    print("\n1) Add a travel destination")
    print("2) Find a travel destination")
    print("3) Remove a travel destination")
    print("4) Sort destinations by alphabet")
    print("5) Count destinations")
    print("6) Exit")
    option = int(input("Choose an option: "))

    if option == 1:
        place = input("Which destination do you want to add? ")
        destinations.append(place)
        print(destinations)
    elif option == 2:
        place = input("Which destination do you want to find? ")
        if place in destinations:
            print("It is at index " + str(destinations.index(place)))
        else:
            print("That destination is not in the list.")
    elif option == 3:
        place = input("Which destination do you want to remove? ")
        if place in destinations:
            destinations.remove(place)
        print(destinations)
    elif option == 4:
        destinations.sort()
        print(destinations)
    elif option == 5:
        print("You have " + str(len(destinations)) + " destinations.")
    elif option == 6:
        print("Goodbye!")
    else:
        print("Invalid option!")
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

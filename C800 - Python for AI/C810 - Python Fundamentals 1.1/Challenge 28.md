---
title: "Challenge #28: Lists - Grocery list"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 28
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #28: Lists - Grocery list

## Problem

Create a program that manages a grocery list for the user:

• Add grocery item
    - Input - item to add
    - Output - new list

• Print grocery list
    - Input - none
    - Output - grocery list printed

• Sort grocery items
    - Input - none
    - Output - sorted list

• Remove grocery item
    - Input- item to remove
    - Output - new list

• Count groceries
    - Input - none
    - Output - number of items in list

• Replace grocery item
    - Input - item to be replace
    - Input - new item to replace with
    - Output - new list

Do as the description states for all menu items. You can have a default list to begin.

## Solutions

```python
groceries = []

option = 0
while option != 4:
    print("\n1) Add grocery item")
    print("2) Print grocery list")
    print("3) Remove grocery item")
    print("4) Exit")
    option = int(input("Choose an option: "))

    if option == 1:
        item = input("What do you want to add? ")
        groceries.append(item)
        print(groceries)
    elif option == 2:
        print(groceries)
    elif option == 3:
        item = input("What do you want to remove? ")
        if item in groceries:
            groceries.remove(item)
        print(groceries)
    elif option == 4:
        print("Goodbye!")
    else:
        print("Invalid option!")
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

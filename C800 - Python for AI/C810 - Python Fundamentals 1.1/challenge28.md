---
title: "Challenge #28: Lists - Grocery list"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 28
challenge_type: "regular"   # regular | supplemental | discontinued
language: python
tags: [python]
author: "Your Name"
status: draft        # todo | draft | reviewed | final
---

# Challenge #28: Lists - Grocery list

## Challenge Brief

https://lms.zebrarobotics.com/courses/2576/assignments/52688

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

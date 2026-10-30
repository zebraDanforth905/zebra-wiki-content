---
title: "Challenge #60: Working with Files - Party Dish Manager"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 60
challenge_type: "regular"   # regular | supplemental | discontinued | optional | unnumbered
language: python
tags: [python]
author: "Your Name"
status: draft        # todo | draft | reviewed | final
---

# Challenge #60: Working with Files - Party Dish Manager

## Challenge Brief

https://lms.zebrarobotics.com/courses/2597/assignments/53243

## Solutions

```python
fileObj = open("party_data.txt", "r")
lines = fileObj.readlines()
fileObj.close()

party = {}
for line in lines:
    line = line.strip()
    if line == "":
        continue
    guest, dish = line.split(":")
    party[guest] = dish

option = 0
while option != 5:
    print("\n1) View all guests and dishes")
    print("2) Add a new guest and dish")
    print("3) Update a guest's dish")
    print("4) Remove a guest")
    print("5) Save and Quit")
    option = int(input("Choose an option: "))

    if option == 1:
        for guest in party:
            print(guest + " is bringing " + party[guest])
    elif option == 2:
        guest = input("Guest name: ")
        dish = input("Dish: ")
        party[guest] = dish
    elif option == 3:
        guest = input("Which guest? ")
        if guest in party:
            party[guest] = input("New dish: ")
        else:
            print("That guest is not on the list.")
    elif option == 4:
        guest = input("Which guest to remove? ")
        if guest in party:
            del party[guest]
    elif option == 5:
        outObj = open("party_data.txt", "w")
        for guest in party:
            outObj.write(guest + ":" + party[guest] + "\n")
        outObj.close()
        print("Saved. Goodbye!")
    else:
        print("Invalid option!")
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

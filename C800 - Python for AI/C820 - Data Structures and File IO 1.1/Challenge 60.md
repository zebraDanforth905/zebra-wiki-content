---
title: "Challenge #60: Working with Files - Party Dish Manager"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 60
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #60: Working with Files - Party Dish Manager

## Problem

You’re organizing a potluck party!
Each guest is bringing one dish, and you want to store this information in a dictionary.

Your Tasks:

1. Read the data from the file and store it in a suitable dictionary.
Each line of the text file contains one guest and one dish, separated by a colon :.
Here’s your default file — party_data.txt:

Alice:Salad
John:Brownies
Maria:Pasta
David:Fruit Platter
Sophie:Cookies
Liam:Pizza
Emma:Sandwiches
Noah:Drinks
Olivia:Guacamole
Ethan:Garlic Bread
Ava:Veggie Wraps
James:Cheese Platter
Isabella:Chocolate Cake
Benjamin:Nachos
Mia:Mini Cupcakes

Hint: Use .split(':') to separate the guest name and the dish when reading the file.

2. Store the data in a dictionary where

•
Keys → Guest names

•
Values → Dishes they brought

Example structure:

{'Alice': 'Salad', 'John': 'Brownies', ...}

3. Create a menu-driven program that lets the user:

• View all guests and dishes

• Add a new guest and dish

• Update a guest’s dish

• Remove a guest

• Save and Quit

4. Save changes back to the file
When the user chooses “Save and Quit”:

• Write all data back to party_data.txt in the same format.

• Display a confirmation message like:

Data saved successfully!

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

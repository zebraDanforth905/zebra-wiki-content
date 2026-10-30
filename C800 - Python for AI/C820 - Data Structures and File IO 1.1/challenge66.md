---
title: "Challenge #66: Methods and Imports - Car class and __str__"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 66
challenge_type: "regular"   # regular | supplemental | discontinued | optional | unnumbered
language: python
tags: [python]
author: "Your Name"
status: draft        # todo | draft | reviewed | final
---

# Challenge #66: Methods and Imports - Car class and __str__

## Challenge Brief

https://lms.zebrarobotics.com/courses/2597/assignments/53249

## Solutions

### CarClass.py

```python
class Car:
    def __init__(self, make, model, year, price, available):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.available = available

    def __str__(self):
        return ("Make: " + self.make +
                "\nModel: " + self.model +
                "\nYear: " + str(self.year) +
                "\nPrice: " + str(self.price) +
                "\nAvailable: " + str(self.available) + "\n")
```

### Inventory.py

```python
from CarClass import Car

inventory = []

option = 0
while option != 3:
    option = int(input("Select an option:\n1) Add a car\n2) List cars\n3) Exit\n"))
    if option == 1:
        make = input("Make: ")
        model = input("Model: ")
        year = int(input("Year: "))
        price = int(input("Price: "))
        available = input("Available (yes/no): ") == "yes"
        inventory.append(Car(make, model, year, price, available))
        print("Car added.")
    elif option == 2:
        for car in inventory:
            print(car)
    elif option == 3:
        print("Goodbye")
    else:
        print("Invalid input!")
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

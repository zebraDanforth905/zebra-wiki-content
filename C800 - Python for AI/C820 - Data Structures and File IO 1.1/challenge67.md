---
title: "Challenge #67: Inheritance and Encapsulation- Motorcycle and Truck"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 67
challenge_type: "regular"   # regular | supplemental | discontinued | optional | unnumbered
language: python
tags: [python]
author: "Your Name"
status: draft        # todo | draft | reviewed | final
---

# Challenge #67: Inheritance and Encapsulation- Motorcycle and Truck

## Challenge Brief

https://lms.zebrarobotics.com/courses/2597/assignments/53250

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

### Motorcycle.py

```python
from CarClass import Car


class Motorcycle(Car):
    # type is "Standard" or "Sport Bike"
    def __init__(self, make, model, year, price, available, type):
        Car.__init__(self, make, model, year, price, available)
        self.type = type

```

### Truck.py

```python
from CarClass import Car


class Truck(Car):
    # type is "Full-size" or "Midsize"; bedSize is "Long bed" or "Short bed"
    def __init__(self, make, model, year, price, available, type, bedSize):
        Car.__init__(self, make, model, year, price, available)
        self.type = type
        self.bedSize = bedSize
```

### Inventory.py

```python
from CarClass import Car
from Motorcycle import Motorcycle
from Truck import Truck

inventory = []

option = 0
while option != 3:
    option = int(input("Select an option:\n1) Add a vehicle\n2) List vehicles\n3) Exit\n"))
    if option == 1:
        kind = input("Car, Motorcycle, or Truck (c/m/t): ")
        make = input("Make: ")
        model = input("Model: ")
        year = int(input("Year: "))
        price = int(input("Price: "))
        available = input("Available (yes/no): ") == "yes"
        if kind == "m":
            type = input("Type (Standard/Sport Bike): ")
            inventory.append(Motorcycle(make, model, year, price, available, type))
        elif kind == "t":
            type = input("Type (Full-size/Midsize): ")
            bedSize = input("Bed size (Long bed/Short bed): ")
            inventory.append(Truck(make, model, year, price, available, type, bedSize))
        else:
            inventory.append(Car(make, model, year, price, available))
        print("Vehicle added.")
    elif option == 2:
        for vehicle in inventory:
            print(vehicle)
    elif option == 3:
        print("Goodbye")
    else:
        print("Invalid input!")
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

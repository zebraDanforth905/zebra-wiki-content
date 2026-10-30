---
title: "Challenge #69: Overriding - Overriding __str__"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 69
challenge_type: "regular"   # regular | supplemental | discontinued | optional | unnumbered
language: python
tags: [python]
author: "Your Name"
status: draft        # todo | draft | reviewed | final
---

# Challenge #69: Overriding - Overriding __str__

## Challenge Brief

https://lms.zebrarobotics.com/courses/2597/assignments/53252

## Solutions

### CarClass.py

```python
class Car:
    def __init__(self, make, model, year, price, available):
        self.make = make
        self.model = model
        self.year = year
        self.__price = price
        self.__available = available

    def getPrice(self):
        return self.__price

    def setPrice(self, newPrice):
        self.__price = newPrice

    def getAvailable(self):
        return self.__available

    def setAvailable(self, newAvailable):
        self.__available = newAvailable

    def __str__(self):
        return ("Make: " + self.make +
                "\nModel: " + self.model +
                "\nYear: " + str(self.year) +
                "\nPrice: " + str(self.__price) +
                "\nAvailable: " + str(self.__available) + "\n")
```

### Motorcycle.py

```python
from CarClass import Car


class Motorcycle(Car):
    # type is "Standard" or "Sport Bike"
    def __init__(self, make, model, year, price, available, type):
        Car.__init__(self, make, model, year, price, available)
        self.type = type

    # Override __str__ to add the Motorcycle's extra attribute
    def __str__(self):
        return Car.__str__(self) + "Type: " + self.type + "\n"
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

    # Override __str__ to add the Truck's extra attributes
    def __str__(self):
        return Car.__str__(self) + "Type: " + self.type + "\nBed Size: " + self.bedSize + "\n"
```

### Inventory.py

```python
from CarClass import Car
from Motorcycle import Motorcycle
from Truck import Truck

inventory = []

option = 0
while option != 4:
    option = int(input("Select an option:\n1) Add a vehicle\n2) List vehicles\n3) Mark a vehicle sold\n4) Exit\n"))
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
        model = input("Enter the model that sold: ")
        for vehicle in inventory:
            if vehicle.model == model:
                vehicle.setAvailable(False)
    elif option == 4:
        print("Goodbye")
    else:
        print("Invalid input!")
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

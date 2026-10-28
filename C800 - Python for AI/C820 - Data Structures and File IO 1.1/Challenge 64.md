---
title: "Challenge #64: OOP - Maintaining data (Car)"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 64
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #64: OOP - Maintaining data (Car)

## Problem

Imagine you work at a car dealership. Your job is to keep track of the inventory, including details like the car’s make, model, year, price, and other features. To make this easier for yourself and your team, you want to create a program that automates inventory management.

You are provided with an inventory file (you may create inventory.txt with these values) that contains all cars in attribute: value format, like this:

Make: Honda
Model: Civic
Year: 2018
Price: 22000
Used: False
Mileage: 30000
Doors: 4
Available: True

Make: Toyota
Model: Corolla
Year: 2020
Price: 25000
Used: True
Mileage: 15000
Doors: 4
Available: True

Make: Ford
Model: Mustang
Year: 2023
Price: 45000
Used: False
Mileage: 0
Doors: 2
Available: False

(Each car is separated by a blank line.)

Car Attributes

Each car has the following attributes:

•
Make – e.g., Honda, Toyota

•
Model – e.g., Civic, Corolla

•
Year – e.g., 2018, 2020

•
Price – CAD price

•
Used – Boolean: True if used, False if new

•
Mileage – in kilometers

•
Doors – number of doors

•
Available – Boolean: True if available for sale

Requirements

•
Define a Car class

• Use the __init__ method to initialize all attributes.

• Use self to store each attribute.

•
Read cars from the inventory file

• Parse each key: value pair.

• Create a Car object for each car.

• Store all car objects in a list called inventory.

•
Build a menu for car salespeople to interact with the inventory. The menu should allow users to:

•
View all cars in the inventory.

•
Add a new car to the inventory.

•
Search for cars by make, model, year, or availability.

•
Remove a car from the inventory.

•
Mark a car as sold (update the Available attribute).

•
Program Structure Requirement

• Your program must use a main() function.

• The main() function should handle the menu loop and user interaction.

• Use helper functions like add_car(), search_car(), remove_car() called from main().

•
Optional Challenges

• Sort the inventory by price, year, or mileage.

• Filter cars based on Used/New status or number of doors.

• Save the updated inventory back to the file for future use.

## Solutions

```python
class Car:
    def __init__(self, make, model, year, price, available):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.available = available

    def __str__(self):
        return (self.make + " " + self.model + " (" + str(self.year) + ")" +
                " - $" + str(self.price) +
                " - Available: " + str(self.available))


inventory = [
    Car("Honda", "Civic", 2020, 25000, True),
    Car("Toyota", "Corolla", 2021, 27000, True),
    Car("Ford", "Mustang", 2019, 40000, False)
]

option = 0
while option != 4:
    print("\n1) List all cars")
    print("2) Find a car by model")
    print("3) Mark a car as sold")
    print("4) Exit")
    option = int(input("Choose an option: "))

    if option == 1:
        for car in inventory:
            print(car)
    elif option == 2:
        model = input("Which model? ")
        for car in inventory:
            if car.model == model:
                print(car)
    elif option == 3:
        model = input("Which model sold? ")
        for car in inventory:
            if car.model == model:
                car.available = False
    elif option == 4:
        print("Goodbye!")
    else:
        print("Invalid option!")
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

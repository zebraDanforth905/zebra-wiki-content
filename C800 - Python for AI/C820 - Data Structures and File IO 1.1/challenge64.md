---
title: "Challenge #64: OOP - Maintaining data (Car)"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 64
challenge_type: "regular"   # regular | supplemental | discontinued | optional | unnumbered
language: python
tags: [python]
author: "Your Name"
status: draft        # todo | draft | reviewed | final
---

# Challenge #64: OOP - Maintaining data (Car)

## Challenge Brief

https://lms.zebrarobotics.com/courses/2597/assignments/53247

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

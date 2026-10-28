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

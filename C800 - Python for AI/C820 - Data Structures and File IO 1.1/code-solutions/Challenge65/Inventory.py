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
            print(car.make, car.model, car.year)
    elif option == 3:
        print("Goodbye")
    else:
        print("Invalid input!")

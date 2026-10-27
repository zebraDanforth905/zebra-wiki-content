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

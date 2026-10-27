animals = {
    "dog": "puppy",
    "cat": "kitten",
    "cow": "calf",
    "horse": "foal",
    "kangaroo": "joey"
}

option = 0
while option != 4:
    print("\n1) See all animals")
    print("2) Look up a baby animal's name")
    print("3) Add a new animal")
    print("4) Exit")
    option = int(input("Choose an option: "))

    match option:
        case 1:
            for animal in animals:
                print(animal + " -> " + animals[animal])
        case 2:
            animal = input("Which animal? ")
            if animal in animals:
                print("A baby " + animal + " is called a " + animals[animal] + ".")
            else:
                print("That animal is not in the dictionary.")
        case 3:
            animal = input("Animal name: ")
            baby = input("Baby name: ")
            animals[animal] = baby
            print("Added!")
        case 4:
            print("Goodbye!")
        case _:
            print("Invalid option!")

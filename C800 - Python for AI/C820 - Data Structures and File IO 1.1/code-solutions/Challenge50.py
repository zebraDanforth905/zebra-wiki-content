items = ["Toy Car", 15, "Doll", 20, "Lego Set", 35, "Book", 10]

total = 0
for i in range(0, len(items), 2):
    name = items[i]
    price = items[i + 1]
    print("Gift: " + name + " - Price: $" + str(price))
    total = total + price

print("Total cost: $" + str(total))

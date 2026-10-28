---
title: "Challenge #70: Overriding -  Online shopping experience"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 70
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #70: Overriding -  Online shopping experience

## Problem

Your goal is to simulate a simple online shopping system in Python using classes and inheritance. You will create two new classes and use method overriding where appropriate.

1. ShoppingCart Class

The ShoppingCart class should keep track of:

• Number of items in the cart

• Names of the items

• Total price

• Price including tax (optional for now, can be ignored in calculations)

Methods to implement:

•
add_item(item) — add an item to the cart

•
remove_item(item) — remove an item from the cart

•
view_cart() — list all items in the cart

•
view_totals() — show total price (and optionally tax)

2. Grocery Class

Each grocery item should store:

• Item name

• Item price

• Item ID (unique identifier)

Methods to implement:

•
__str__() — return a readable string showing the item’s name, price, and ID

• Any other methods needed to support adding/removing items to/from the cart

3. Program Requirements

• Start by greeting the user.

• Display a list of grocery items they can choose from.

• Let the user add items to the cart or remove them.

• Let the user view their cart and totals at any time.

• Use inheritance if you see opportunities for shared behavior.

• Use method overriding to customize how objects are printed (__str__) or how totals are displayed.

Example Interaction

Welcome to the Online Grocery Store!

Available Items:
1. Apple - $1.50
2. Bread - $2.00
3. Milk - $3.00

What would you like to do?
1. Add item to cart
2. Remove item from cart
3. View cart
4. View totals
5. Checkout

> 1
Enter item ID to add: 1
Apple added to your cart!

> 3
Items in your cart:
Apple - $1.50

> 4
Total price: $1.50

Hints for Implementation

• The ShoppingCart class can store a list of Grocery objects.

• Override __str__ in Grocery to display items nicely.

• Use methods in ShoppingCart to update the number of items and total price automatically.

• Optional: add tax calculations in view_totals() or in a separate overridden method.

## Solutions

```python
# An online shopping example that uses inheritance and method overriding.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # The base description. Child classes will override this.
    def describe(self):
        return self.name + " - $" + str(self.price)


class Book(Product):
    def __init__(self, name, price, author):
        Product.__init__(self, name, price)
        self.author = author

    # Override describe() to include the author
    def describe(self):
        return self.name + " by " + self.author + " - $" + str(self.price)


class Electronic(Product):
    def __init__(self, name, price, warranty):
        Product.__init__(self, name, price)
        self.warranty = warranty

    # Override describe() to include the warranty
    def describe(self):
        return (self.name + " - $" + str(self.price) +
                " (" + str(self.warranty) + " year warranty)")


store = [
    Book("The Hobbit", 15, "J.R.R. Tolkien"),
    Electronic("Headphones", 80, 2),
    Product("Coffee Mug", 10)
]

cart = []
total = 0
for product in store:
    print(product.describe())
    cart.append(product)
    total = total + product.price

print("\nYour cart total is $" + str(total))
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

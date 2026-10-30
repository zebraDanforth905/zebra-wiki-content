---
title: "Challenge #70: Overriding -  Online shopping experience"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 70
challenge_type: "regular"   # regular | supplemental | discontinued | optional | unnumbered
language: python
tags: [python]
author: "Your Name"
status: draft        # todo | draft | reviewed | final
---

# Challenge #70: Overriding -  Online shopping experience

## Challenge Brief

https://lms.zebrarobotics.com/courses/2597/assignments/53253

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

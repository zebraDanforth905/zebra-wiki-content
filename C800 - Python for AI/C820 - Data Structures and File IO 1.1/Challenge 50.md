---
title: "Challenge #50: The Mystery Gift Box"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 50
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #50: The Mystery Gift Box

## Problem

You are given a list that mixes gift names and their prices:

items = ["Toy Car", 15, "Doll", 20, "Lego Set", 35, "Book", 10]

Task:
Write code that loops through the list and prints:

Gift: Toy Car - Price: $15
Gift: Doll - Price: $20
Gift: Lego Set - Price: $35
Gift: Book - Price: $10

Hint:
Every even index is a name, and the next index is its price.
Use iteration and range() smartly!

Bonus:
Add a feature that calculates and displays the total cost at the end.

## Solutions

```python
items = ["Toy Car", 15, "Doll", 20, "Lego Set", 35, "Book", 10]

total = 0
for i in range(0, len(items), 2):
    name = items[i]
    price = items[i + 1]
    print("Gift: " + name + " - Price: $" + str(price))
    total = total + price

print("Total cost: $" + str(total))
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

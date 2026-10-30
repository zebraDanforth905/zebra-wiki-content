---
title: "Challenge #50: The Mystery Gift Box"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 50
challenge_type: "regular"   # regular | supplemental | discontinued | optional | unnumbered
language: python
tags: [python]
author: "Your Name"
status: draft        # todo | draft | reviewed | final
---

# Challenge #50: The Mystery Gift Box

## Challenge Brief

https://lms.zebrarobotics.com/courses/2597/assignments/53233

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

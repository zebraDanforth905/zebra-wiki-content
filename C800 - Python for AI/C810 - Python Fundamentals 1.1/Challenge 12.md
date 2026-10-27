---
title: "Challenge #12: Turtle - Circle"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 12
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #12: Turtle - Circle

## Problem

You will be using the Turtle module for this challenge.

Draw a circle based on user input, similar to the instructions before, but use the user input for the radius of the circle. To draw a circle, you can use the circle() function. This function takes a single number as its input, which defines the radius of the circle. For example, turtle.circle(x), where x is the radius used to draw a circle of the specified size.

## Solutions

```python
import turtle

radius = int(input("Enter the radius of the circle: "))

marty = turtle.Turtle()
marty.circle(radius)

turtle.done()
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

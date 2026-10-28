---
title: "Challenge #49: Functions -  Drawing a shape"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 49
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #49: Functions -  Drawing a shape

## Problem

Your program must:

•
Ask the user what shape they want to draw:

• circle

• square

• triangle

•
Ask the user for:

• the size of the shape

• the color of the shape

•
Use at least four functions, including:

• A main function that runs the overall program

• Additional helper functions (e.g., one for each shape)

• Inside your main function, use a match statement to call the correct shape-drawing function based on the user’s input.

Sample input:

Resulting output:

## Solutions

```python
import turtle

marty = turtle.Turtle()


def draw_circle(size, color):
    marty.color(color)
    marty.begin_fill()
    marty.circle(size)
    marty.end_fill()


def draw_square(size, color):
    marty.color(color)
    marty.begin_fill()
    for side in range(4):
        marty.forward(size)
        marty.left(90)
    marty.end_fill()


def draw_triangle(size, color):
    marty.color(color)
    marty.begin_fill()
    for side in range(3):
        marty.forward(size)
        marty.left(120)
    marty.end_fill()


def main():
    shape = input("What shape do you want (circle/square/triangle)? ")
    size = int(input("What size? "))
    color = input("What color? ")

    match shape:
        case "circle":
            draw_circle(size, color)
        case "square":
            draw_square(size, color)
        case "triangle":
            draw_triangle(size, color)
        case _:
            print("That is not a shape I know.")

    turtle.done()


main()
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

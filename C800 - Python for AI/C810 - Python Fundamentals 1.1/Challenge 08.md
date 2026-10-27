---
title: "Challenge #08: Turtle - Triangle"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 8
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #08: Turtle - Triangle

## Problem

🖌️ How to Fill a Shape in Turtle

To fill shapes in Turtle, we use two functions:

Function
Purpose

begin_fill()
Tells Turtle to start recording the shape outline

end_fill()
Fills the shape drawn between begin_fill() and end_fill()

⚠️ Important:
Everything drawn between begin_fill() and end_fill() will be filled with the active fill color.

Example:

import turtle

screen = turtle.Screen()
pen = turtle.Turtle()

pen.fillcolor("yellow")   # Set fill color
pen.begin_fill()          # Start filling
pen.circle(80)            # Draw a circle
pen.end_fill()            # End filling

pen.hideturtle()
screen.exitonclick()

Challenge :

A triangle where all the sides are of the same length is called an equilateral triangle. For this challenge, draw an equilateral triangle and fill it with a color. Save the code in a file called Challenge8.py.

## Solutions

```python
import turtle

marty = turtle.Turtle()

marty.begin_fill()
marty.forward(100)
marty.left(120)
marty.forward(100)
marty.left(120)
marty.forward(100)
marty.end_fill()

turtle.done()
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

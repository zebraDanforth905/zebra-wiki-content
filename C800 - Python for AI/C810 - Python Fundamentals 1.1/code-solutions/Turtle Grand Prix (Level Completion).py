import turtle
import random

# Set up the race screen
screen = turtle.Screen()
screen.setup(700, 500)
screen.title("The Great Turtle Grand Prix")
screen.bgcolor("lightyellow")

FINISH_LINE = 300

# Draw the finish line
marker = turtle.Turtle()
marker.hideturtle()
marker.penup()
marker.color("black")
marker.goto(FINISH_LINE, 220)
marker.pendown()
marker.goto(FINISH_LINE, -220)

# Title banner
banner = turtle.Turtle()
banner.hideturtle()
banner.penup()
banner.goto(0, 230)
banner.write("The Great Turtle Grand Prix!", align="center", font=("Arial", 18, "bold"))

# Create six racers, each in its own lane
colors = ["red", "blue", "green", "purple", "orange", "brown"]
racers = []
lane = 150
for color in colors:
    racer = turtle.Turtle()
    racer.shape("turtle")
    racer.color(color)
    racer.penup()
    racer.goto(-300, lane)
    lane = lane - 60
    racers.append(racer)

# Run the race: move each turtle forward by a random amount each round
winner = None
while winner is None:
    for racer in racers:
        racer.forward(random.randint(0, 20))
        if racer.xcor() >= FINISH_LINE:
            winner = racer
            break

# Announce the winner
banner.goto(0, -240)
banner.color(winner.color()[0])
banner.write("The " + winner.color()[0] + " turtle wins!", align="center", font=("Arial", 18, "bold"))

screen.exitonclick()

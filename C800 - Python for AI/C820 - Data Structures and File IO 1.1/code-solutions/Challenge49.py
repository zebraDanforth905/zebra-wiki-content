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

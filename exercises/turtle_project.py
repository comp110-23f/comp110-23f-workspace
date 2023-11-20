"""For this project, I decided to draw a turtle."""
__author__ = "730402747"

from turtle import Turtle, done


def main() -> None:
    """The entrypoint of my scene. I define my variables here."""
    turt: Turtle = Turtle()
    x = 100
    y = 50
    r = 100
    make_shell(turt, x, y, r)
    turtle_legs(turt, x, y, r)
    turtle_tail(turt, x, y, r)
    make_shell(turt, x, y, r / 2)
    turtle_head(turt, x, y, r)
    done()


def turtle_tail(turt: Turtle, x: float, y: float, r: float) -> None:
    """This adds a triangle tail to start drawing the turtle."""
    a: float = .7 * r
    turt.penup()
    turt.goto(x, y)
    turt.setheading(0)
    turt.right(67.5)
    turt.forward(1.207 * r)
    turt.right(90)
    turt.forward(a / 2)
    turt.left(120)
    turt.pendown()
    turt.forward(a)
    turt.left(120)
    turt.forward(a)


def turtle_legs(turt: Turtle, x: float, y: float, r: float) -> None:
    """This draws the circle legs that are on the turtles body."""
    a: float = .375 * r
    i = 0
    while i <= 315:
        turt.setheading(i)
        turt.penup()
        turt.goto(x, y)
        turt.right(22.5)
        turt.forward(r)
        turt.right(90)
        turt.circle(a, 60)
        turt.pendown()
        turt.circle(a, 240)
        i += 90


def make_shell(turt: Turtle, x: float, y: float, r: float) -> None:
    """This creates a green hexagon that will be the turtles body."""
    color: float = 0.2
    turt.fillcolor(0, color, 0)
    turt.penup()
    turt.goto(x, y - 1.307 * r)
    turt.begin_fill()
    turt.pendown()
    i = 22.5
    while i <= 360:
        turt.setheading(i)
        turt.forward(r)
        i += 45
    turt.end_fill()


def turtle_head(turt: Turtle, x: float, y: float, r: float) -> None:
    """Draws a rectangular and semi circle to be the turtles head with a green filled in color."""
    color: float = 0.5
    turt.fillcolor(0, color, 0)
    turt.begin_fill()
    a: float = .4 * r
    turt.penup()
    turt.goto(x, y + 1.307 * r)
    turt.setheading(202.5)
    turt.forward(.1 * r)
    turt.right(90)
    turt.pendown()
    turt.begin_fill()
    turt.forward(a)
    turt.circle(a, 180)
    turt.forward(a)
    turt.left(90)
    turt.forward(2 * a)
    turt.end_fill()


if __name__ == "__main__":
    main()
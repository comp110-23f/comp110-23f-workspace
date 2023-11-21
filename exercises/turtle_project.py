"""My turtle art project!"""
from turtle import Turtle, colormode, done

colormode(255)


def move_davinci(turtle: Turtle, x_cor: int, y_cor: int) -> None:
    """Moves the davinci turtle with the whole penup-pendown procedure."""
    turtle.penup()
    turtle.goto(x_cor, y_cor)
    turtle.pendown()


def draw_forest(turtle: Turtle, width: int, height: int) -> None:
    """Draws the rectangle representing the forest."""
    turtle.begin_fill()
    turtle.fillcolor("green")
    for index in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()


def draw_tree_lines(turtle: Turtle, increments: int, segment_length: int, left: int, bottom: int, height_limiter: int) -> None:
    """Draws the tree lines to represent the tops of trees in a forest."""
    curr_height: int = bottom
    while (curr_height < height_limiter + bottom):
        move_davinci(turtle, left, curr_height)
        for index in range(increments):
            turtle.left(30)
            turtle.forward(segment_length)
            turtle.right(60)
            turtle.forward(segment_length)
            turtle.left(30)
        curr_height += 60


def draw_sky_gradient(turtle: Turtle, start_width: int, band_length: int, start_height: int, end_height: int, r_val: float, g_val: float, b_val: float) -> None:
    """Draws a sky section which blends the color from a red to a yellow orange color as height increases."""
    curr_height: int = start_height
    init_g_val: float = g_val
    while (curr_height < end_height):
        move_davinci(turtle, start_width, curr_height)
        turtle.color(r_val, init_g_val, b_val)
        turtle.forward(band_length)
        curr_height += 1
        if (init_g_val < 255 and curr_height % 2 == 0):
            init_g_val += 1
    turtle.color("black")


def draw_lake(turtle: Turtle, increments: int, segment_length: int, angle: float, x_cor: int, y_cor: int) -> None:
    """Draws the lake at the bottom of the screen."""
    turtle.left(60)
    turtle.begin_fill()
    turtle.fillcolor(40, 159, 255)
    for index in range(increments):
        turtle.right(angle)
        turtle.forward(segment_length)
    turtle.goto(x_cor, y_cor)
    turtle.end_fill()
    turtle.left(239)


def draw_back_mountain_range(turtle: Turtle, increments: int, segment_length: int, left: int, mountain_base: int) -> None:
    """Draws the first layer of mountains."""
    turtle.right(239)
    move_davinci(turtle, left, mountain_base)
    
    turtle.begin_fill()
    turtle.fillcolor(65, 145, 222)
    for index in range(increments):
        turtle.forward(segment_length + 7)
        turtle.left(120)
        turtle.forward(segment_length)
        turtle.right(120)
    turtle.right(120)
    turtle.goto(-left, mountain_base - (segment_length - 47))
    turtle.goto(left, mountain_base - (segment_length - 47))
    turtle.end_fill()
    turtle.right(180)
    

def draw_front_mountain_range(turtle: Turtle, increments: int, segment_length: int, left: int, mountain_base: int) -> None:
    """Draws the second layer of mountains."""
    move_davinci(turtle, left, mountain_base)
    turtle.begin_fill()
    turtle.fillcolor(16, 116, 213)
    for index in range(increments):
        turtle.left(60)
        turtle.forward(segment_length)
        turtle.right(120)
        turtle.forward(segment_length + 8)
        turtle.left(60)
    turtle.right(180)
    turtle.goto(left, mountain_base)
    turtle.end_fill()


def draw_sun(turtle: Turtle, x_cor: int, y_cor: int, radius: int) -> None:
    """Draws the sun circle."""
    move_davinci(turtle, x_cor, y_cor)
    turtle.begin_fill()
    turtle.fillcolor(253, 255, 115)
    turtle.circle(radius)
    turtle.end_fill()


def main() -> None:
    """The entrypoint of my scene."""
    davinci: Turtle = Turtle()
    davinci.screen.bgcolor("white")
    davinci.speed(0)
    davinci.hideturtle()
    davinci.screen.tracer(False)
    screen_bottom: int = -davinci.screen.window_height() // 2
    screen_left: int = (-davinci.screen.window_width() // 2) - 10
    lake_increments: int = 290
    lake_segment_length: int = 4
    lake_angle: float = 0.41
    forest_width: int = davinci.screen.window_width() + 10
    forest_height: int = 330
    tree_line_increment: int = 19
    tree_line_segment_length: int = 30
    mountain_base_height: int = screen_bottom + forest_height
    mountain_line_segment_length: int = 350
    front_mountain_increment: int = 3
    back_mountain_increment: int = 3
    moon_radius: int = 60

    move_davinci(davinci, screen_left, screen_bottom)
    draw_forest(davinci, forest_width, forest_height)
    move_davinci(davinci, screen_left, screen_bottom)
    draw_tree_lines(davinci, tree_line_increment, tree_line_segment_length, screen_left, screen_bottom, forest_height)
    move_davinci(davinci, screen_left, screen_bottom)
    draw_lake(davinci, lake_increments, lake_segment_length, lake_angle, screen_left, screen_bottom)
    draw_sky_gradient(davinci, screen_left, screen_left * 2, mountain_base_height, -screen_bottom, 249, 0, 80)
    draw_back_mountain_range(davinci, back_mountain_increment, mountain_line_segment_length, screen_left, mountain_base_height + 303)
    draw_front_mountain_range(davinci, front_mountain_increment, mountain_line_segment_length, screen_left, mountain_base_height)
    draw_sun(davinci, 0, 370, moon_radius)
    move_davinci(davinci, 0, 0)
    done()


if __name__ == "__main__":
    main()
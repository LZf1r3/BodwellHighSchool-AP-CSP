import random as r
import turtle
from itertools import cycle
import math

# -------------------------------
# INITIAL SETUP
# -------------------------------

screen = turtle.Screen()
screen.screensize(800, 600)
t = turtle.Turtle()
t.speed(0)


# -------------------------------
# BASIC SHAPES AND UTILITIES
# -------------------------------

def draw_rectangle_fill(t, x, y, width, height, color):
    """Draw a filled rectangle at (x, y) with given dimensions and color."""
    t.setheading(0)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()


def draw_circle(t, x, y, radius, fillcolor=None, outline=True):
    """Draw a circle centered at (x, y) with optional fill and outline."""
    t.up()
    t.goto(x, y - radius)
    t.down()
    if fillcolor:
        t.fillcolor(fillcolor)
        t.begin_fill()
    if not outline:
        t.pencolor(t.fillcolor())
    t.circle(radius)
    if fillcolor:
        t.end_fill()
    t.up()


def draw_rectangle(t, x, y, w, h, color):
    """Draw a filled rectangle using the turtle."""
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.color(color)
    t.pendown()
    t.begin_fill()
    for _ in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
    t.end_fill()
    t.up()


def margin(x_screen, y_screen, color):
    """Draw a border/margin around the entire screen."""
    t.setheading(0)
    t.penup()
    t.goto(-x_screen / 2, -y_screen / 2)
    t.pendown()
    t.color(color)
    t.pensize(10)
    for _ in range(2):
        t.forward(x_screen)
        t.left(90)
        t.forward(y_screen)
        t.left(90)
    t.pensize(1)

# -------------------------------
# BACKGROUND AND ENVIRONMENT
# -------------------------------

def background():
    """Draw a vertical gradient sky background."""
    start_pos = (-400, 300)
    end_pos = (400, -300)
    start_color = (15, 19, 76)
    end_color = (51, 61, 171)

    x_distance = end_pos[0] - start_pos[0]
    y_distance = end_pos[1] - start_pos[1]
    increment_color = tuple(
        (end - start) / abs(y_distance) for end, start in zip(end_color, start_color)
    )

    t.penup()
    t.goto(start_pos)
    t.speed(9)
    t.pendown()
    heading = cycle([0, 270, 180, 270])

    for i in range(abs(y_distance)):
        color = (int(i * inc) + start for inc, start in zip(increment_color, start_color))
        t.color("#{:0>2X}{:0>2X}{:0>2X}".format(*color))
        t.seth(next(heading))
        t.forward(x_distance)
        t.seth(next(heading))
        t.forward(1)


def draw_snowflakes(t):
    """Draw random snowflakes in the sky."""
    for _ in range (85):
        t.penup()
        t.color("white")
        x = r.randint(-400,400)
        y = r.randint(-100,300)
        t.goto(x,y)
        t.pendown()
        arms = r.randint(6,9)
        angle = 360/arms
        size = r.randint(3,10)
        for _ in range(arms):
            t.forward(size)

            # simple side spikes
            t.backward(size * 0.3)
            t.left(45)
            t.forward(size * 0.2)
            t.backward(size * 0.2)
            t.right(90)
            t.forward(size * 0.2)
            t.backward(size * 0.2)
            t.left(45)

            t.backward(size)
            t.right(angle)


def draw_snowflakes_ground(t):
    """Draw dense snowflakes covering the ground for realism."""
    for count, (range_y, num) in enumerate(
        [((-300, -150), 10000), ((-250, -200), 300), ((-200, -150), 750)]
    ):
        for _ in range(num):
            t.penup()
            t.color("white")
            _x = r.randint(-400, 400)
            _y = r.randint(*range_y)
            t.goto(_x, _y)
            t.pendown()
            arms = r.randint(6, 9)
            angle = 360 / arms
            size = r.randint(3, 9)
            for _ in range(arms):
                t.forward(size)
                # Side spikes
                t.backward(size * 0.3)
                t.left(45)
                t.forward(size * 0.2)
                t.backward(size * 0.2)
                t.right(90)
                t.forward(size * 0.2)
                t.backward(size * 0.2)
                t.left(45)
                t.backward(size)
                t.right(angle)


# -------------------------------
# CLOUDS AND SKY ELEMENTS
# -------------------------------

def draw_fuzzy_cloud(t, x, y, scale=1, puffs=20):
    """Draw a fluffy cloud using overlapping circles."""
    t.color("white")
    t.fillcolor("white")
    for _ in range(puffs):
        offset_x = r.randint(-40, 40) * scale
        offset_y = r.randint(-20, 20) * scale
        t.penup()
        t.goto(x + offset_x, y + offset_y)
        t.pendown()
        radius = r.randint(15, 35) * scale
        t.begin_fill()
        t.circle(radius)
        t.end_fill()


def clouds(t, number):
    """Draw a specified number of random clouds in the sky."""
    for _ in range(number):
        draw_fuzzy_cloud(t, r.randint(-400, 400), r.randint(150, 200))


# -------------------------------
# OBJECTS (TREE, STAR, SNOWMAN, CABIN, GIFTS)
# -------------------------------

def draw_triangle(x, y, width, height, color):
    """Draw a triangle used for tree layers."""
    t.goto(x, y)
    t.color(color)
    t.begin_fill()
    t.setheading(0)
    t.forward(width / 2)
    t.left(120)
    t.forward(width)
    t.left(120)
    t.forward(width)
    t.left(120)
    t.forward(width / 2)
    t.end_fill()


def draw_christmas_tree():
    """Draw a layered Christmas tree with trunk."""
    layers = [
        (-300, -110, 200, 120, "#0b6623"),  # bottom
        (-300, -40, 160, 100, "#0d7a2a"),   # middle
        (-300, 20, 120, 80, "#0e8f33"),     # top
    ]
    for x, y, w, h, color in layers:
        draw_triangle(x, y, w, h, color)

    # Tree trunk
    t.goto(-315, -160)
    t.color("#5a3e2b")
    t.begin_fill()
    for _ in range(2):
        t.forward(30)
        t.left(90)
        t.forward(50)
        t.left(90)
    t.end_fill()


def draw_centered_star(t, x, y, size):
    """Draw a glowing 5-pointed star."""
    draw_circle(t, x + 25, y - 8, size / 5, "#FAE628")
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("#FFEC00")
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()
    t.color("black")


def draw_snowman(t, x, y):
    """Draw a snowman with circles, carrot nose, eyes, and arms."""
    draw_circle(t, x, y, 20, "white")
    draw_circle(t, x, y + 30, 15, "white")
    draw_circle(t, x, y + 50, 10, "white")
    # Eyes
    draw_circle(t, x - 4, y + 55, 2, "black")
    draw_circle(t, x + 4, y + 55, 2, "black")
    # Carrot nose
    t.penup()
    t.goto(x, y + 50)
    t.pendown()
    t.color("orange")
    t.begin_fill()
    for _ in range(3):
        t.forward(5)
        t.left(120)
    t.end_fill()
    # Buttons
    for i in range(3):
        draw_circle(t, x, y + 20 + i * 10, 2, "black")
    # Arms
    for direction in [-1, 1]:
        t.penup()
        t.goto(x + 15 * direction, y + 30)
        t.pendown()
        t.setheading(20 * direction)
        t.forward(20)


def draw_window(t, x, y, w, h):
    """Draw a house window with grid panes."""
    draw_rectangle(t, x, y, w, h, "#C29606")
    t.color("black")
    t.width(2)
    # Cross pattern
    t.penup()
    t.goto(x + w / 2, y)
    t.pendown()
    t.goto(x + w / 2, y + h)
    t.penup()
    t.goto(x, y + h / 2)
    t.pendown()
    t.goto(x + w, y + h / 2)
    t.width(1)


def draw_gifts():
    """Draw wrapped Christmas gifts with ribbons and bows."""
    gift_data = [
        (-370, -148, 30, 25, 'red', 'gold'),
        (-340, -155, 25, 30, '#00CED1', 'white'),
        (-310, -150, 28, 22, 'green', 'red'),
        (-280, -145, 35, 30, 'purple', 'gold')
    ]
    for x, y, width, height, box_color, ribbon_color in gift_data:
        draw_rectangle(t, x, y, width, height, box_color)
        t.color(ribbon_color)
        t.width(3)
        # Vertical ribbon
        t.penup()
        t.goto(x + width / 2, y)
        t.pendown()
        t.goto(x + width / 2, y + height)
        # Horizontal ribbon
        t.penup()
        t.goto(x, y + height / 2)
        t.pendown()
        t.goto(x + width, y + height / 2)
        t.width(1)
        # Bow
        t.penup()
        t.goto(x + width / 2, y + height)
        t.dot(8, ribbon_color)
    t.color("black")


def draw_cabin(t, x, y, width, height):
    """Draw a cozy cabin with chimney, door, roof, and window."""
    roof_height = height * 0.5
    door_width, door_height = width * 0.2, height * 0.4
    door_x, door_y = x + (width - door_width) / 2, y
    chimney_width, chimney_height = width * 0.15, height * 0.4
    chimney_x, chimney_y = x + width * 0.75, y + height + roof_height * 0.15
    win_width, win_height = width * 0.25, height * 0.25
    win_x, win_y = x + width * 0.1, y + height * 0.5

    draw_rectangle(t, x, y, width, height, "#6b3f27")  # Cabin body
    draw_rectangle(t, door_x, door_y, door_width, door_height, "#3e2723")  # Door

    # Chimney smoke
    for i in range(5):
        smoke_x = chimney_x + chimney_width / 2 + r.randint(-10, 10)
        smoke_y = chimney_y + chimney_height + i * 15
        smoke_radius = r.randint(8, 15)
        draw_circle(t, smoke_x, smoke_y, smoke_radius, "lightgray", outline=False)
    draw_rectangle(t, chimney_x, chimney_y, chimney_width, chimney_height, "#5a3e2b")

    draw_circle(t, door_x + door_width - 10, door_y + door_height / 2, 3, "gold")  # Knob

    # Roof
    t.penup()
    t.goto(x, y + height)
    t.pendown()
    t.color("#8b4513")
    t.begin_fill()
    t.goto(x + width / 2, y + height + roof_height)
    t.goto(x + width, y + height)
    t.goto(x, y + height)
    t.end_fill()

    draw_window(t, win_x, win_y, win_width, win_height)  # Window

    # Window frame
    t.color("#c9a36b")
    t.width(3)
    t.up()
    t.goto(win_x, win_y)
    t.setheading(0)
    t.down()
    for _ in range(2):
        t.forward(win_width)
        t.left(90)
        t.forward(win_height)
        t.left(90)
    t.up()
    # Window crossbars
    t.goto(win_x + win_width / 2, win_y)
    t.setheading(90)
    t.down()
    t.forward(win_height)
    t.up()
    t.goto(win_x, win_y + win_height / 2)
    t.setheading(0)
    t.down()
    t.forward(win_width)
    t.up()


# -------------------------------
# MAIN EXECUTION
# -------------------------------

if __name__ == "__main__":
    screen.tracer(0)
    
    # Draw background and clouds
    background()
    clouds(t, 6)

    # Draw ground
    draw_rectangle_fill(t, -400, -300, 800, 150, "darkgreen")

    # Draw cabin, tree, decorations, and snowman
    draw_cabin(t, 200, -150, 200, 125)
    draw_christmas_tree()
    draw_centered_star(t, -325, 140, 50)
    
    # Draw snowflakes
    draw_snowflakes(t)
    draw_snowflakes_ground(t)
    
    # Draw extra ekements (snowman n gifts)
    draw_gifts()
    draw_snowman(t, -180, -150)

    # Frame border
    margin(800, 600, "#42220E")

    # Finalize drawing
    screen.update()
    screen.exitonclick()

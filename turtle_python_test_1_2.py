<<<<<<< Updated upstream
=======
import turtle

def draw_rectangular_gift(x, y, width=150, height=100, box_color="red", ribbon_color="gold"):
    """
    Draws a rectangular gift.
    
    x, y           -> center of the gift
    width, height  -> dimensions of the box
    box_color      -> box color
    ribbon_color   -> ribbon and bow color
    """
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)

    half_w = width / 2
    half_h = height / 2
    ribbon_w = min(width, height) * 0.15
    bow_size = min(width, height) * 0.15

    # --- Draw box ---
    t.penup()
    t.goto(x - half_w, y - half_h)
    t.pendown()
    t.color(box_color)
    t.fillcolor(box_color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

    # --- Vertical ribbon ---
    t.penup()
    t.goto(x - ribbon_w/2, y - half_h)
    t.pendown()
    t.color(ribbon_color)
    t.fillcolor(ribbon_color)
    t.begin_fill()
    for _ in range(2):
        t.forward(ribbon_w)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

    # --- Horizontal ribbon ---
    t.penup()
    t.goto(x - half_w, y - ribbon_w/2)
    t.pendown()
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(ribbon_w)
        t.left(90)
    t.end_fill()

    # --- Simple bow ---
    t.penup()
    t.goto(x, y + half_h)
    t.pendown()
    t.begin_fill()
    t.circle(bow_size, 180)  # left loop
    t.end_fill()

    t.penup()
    t.goto(x, y + half_h)
    t.pendown()
    t.begin_fill()
    t.circle(-bow_size, 180)  # right loop
    t.end_fill()

import turtle

draw_rectangular_gift(0, 0, width=180, height=100, box_color="#d62828", ribbon_color="#f5d142")
draw_rectangular_gift(-200, -50, width=120, height=80, box_color="#2a9d8f", ribbon_color="#ffd166")
draw_rectangular_gift(200, -30, width=100, height=60, box_color="#90be6d", ribbon_color="#f4e285")

turtle.done()
>>>>>>> Stashed changes

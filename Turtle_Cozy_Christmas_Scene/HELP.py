import random as r
import turtle
from itertools import cycle
import math as mt
screen = turtle.Screen()
screen.screensize(800,600)
t = turtle.Turtle()

t.speed(0)

def draw_rectangle_fill(t,x,y,width,height,color):
    t.setheading(0)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(2):  # Draw two pairs of sides
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

#Function taken from Mr. Gunn and transformed to properly draw gradient background
def background():
    start_pos = -400, 300
    end_pos = 400, -300
    start_color = 15, 19, 76
    end_color = 51, 61, 171

    x_distance = end_pos[0] - start_pos[0]
    y_distance = end_pos[1] - start_pos[1]
    increment_color = tuple((end - start) / abs(y_distance) for end, start in zip(end_color, start_color))

    t.penup()
    t.goto(start_pos)
    t.speed(9)
    t.pendown()
    heading = cycle([0, 270, 180, 270])
    for i in range(abs(y_distance)):
        color = (int(i*inc)+start for inc, start in zip(increment_color, start_color))
        t.color("#{:0>2X}{:0>2X}{:0>2X}".format(*color))
        t.seth(next(heading))
        t.forward(x_distance)
        t.seth(next(heading))
        t.forward(1)

def draw_snowflakes(t):
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
    for _ in range (10000):
        t.penup()
        t.color("white")
        _x = r.randint(-400,400)
        _y = r.randint(-300,-150)
        t.goto(_x,_y)
        t.pendown()
        arms = r.randint(6,9)
        angle = 360/arms
        size = r.randint(3,6)
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

    for _ in range (300):
        t.penup()
        t.color("white")
        _x = r.randint(-400,400)
        _y = r.randint(-250,-200)
        t.goto(_x,_y)
        t.pendown()
        arms = r.randint(6,9)
        angle = 360/arms
        size = r.randint(3,7)
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

    for _ in range (750):
        t.penup()
        t.color("white")
        _x = r.randint(-400,400)
        _y = r.randint(-200,-150)
        t.goto(_x,_y)
        t.pendown()
        arms = r.randint(6,9)
        angle = 360/arms
        size = r.randint(3,9)
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

    

#functions to draw house
def draw_walls(t,x,y,width,height,color):
    t.setheading(0)
    t.penup()
    t.goto(x,y)
    t.pendown()
    
    draw_rectangle_fill(t,x,y,width,height,color)

def draw_roof(t,x,y,width,color):
    t.setheading(0)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(color)

    t.forward(width_house+20)
    t.left(135)
    t.forward(width)
    t.left(90)
    t.forward(width)

def draw_circle(t, x, y, radius, fillcolor=None, outline=True):
    t.up()
    t.goto(x, y - radius)   # turtle draws circle from center offset
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

def margin(x_screen, y_screen ,color):
    t.setheading(0)
    t.penup()
    t.goto(-x_screen/2,-y_screen/2)
    t.pendown()

    t.color(color)
    t.pensize(10)
    for _ in range(2):
        t.forward(x_screen)
        t.left(90)
        t.forward(y_screen)
        t.left(90)

def draw_hat(t,x,y):
    t.penup()
    t.goto(x,y)
    t.setheading(0)
    t.pendown()

    t.color("black")
    t.begin_fill()
    t.forward(18)
    t.left(90)
    t.forward(6)
    t.left(90)
    t.forward(10)
    t.right(90)
    t.forward(5)
    t.left(90)
    t.forward(16)
    t.left(90)
    t.forward(5)
    t.right(90)
    t.forward(10)
    t.left(90)
    t.forward(6)
    t.left(90)
    t.forward(18)
    t.end_fill()

def draw_fuzzy_cloud(t, x, y, scale=1, puffs=20):
    """
    Draws a fuzzy, fluffy cloud made of many random circles.
    - t: turtle
    - x, y: center
    - scale: size of cloud
    - puffs: number of fuzzy circles
    """
    t.color("white")
    t.fillcolor("white")
    t.penup()
    t.goto(x, y)
    t.pendown()

    for _ in range(puffs):
        # Random small offsets for fuzziness
        offset_x = r.randint(-40, 40) * scale
        offset_y = r.randint(-20, 20) * scale

        t.penup()
        t.goto(x + offset_x, y + offset_y)
        t.pendown()

        # Random radius for more organic shape
        radius = r.randint(15, 35) * scale

        t.begin_fill()
        t.circle(radius)
        t.end_fill()

def draw_triangle(x, y, width, height, color):
    t.goto(x, y)
    t.color(color)
    t.begin_fill()

    t.setheading(0)
    t.forward(width/2)
    t.left(120)
    t.forward(width)
    t.left(120)
    t.forward(width)
    t.left(120)
    t.forward(width/2)

    t.end_fill()

def draw_christmas_tree():
    t.penup()
    # Tree layers (big → small)
    layers = [
        (-300, -110, 200, 120, "#0b6623"),  # bottom
        (-300, -40, 160, 100, "#0d7a2a"),   # middle
        (-300, 20, 120, 80, "#0e8f33"),      # top
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

def clouds(t,number):
    for _ in range(number):
        draw_fuzzy_cloud(t,r.randint(-400,400),r.randint(150,200))

def draw_gift(x, y, width=80, height=60, box_color="#d62828", ribbon_color="#fcbf49"):
    """
    Draws a wrapped gift with ribbon and a bow.
    
    Parameters:
        x, y          – center of the gift box
        width, height – size of the box
        box_color     – color of the box
        ribbon_color  – color of the ribbon/bow
    """
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()
    
    # Move to bottom-left corner
    t.goto(x - width/2, y - height/2)
    
    # --- Draw the box ---
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
    t.color(ribbon_color)
    t.fillcolor(ribbon_color)
    
    t.goto(x - width*0.1, y - height/2)
    t.begin_fill()
    for _ in range(2):
        t.forward(width*0.2)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()
    
    # --- Horizontal ribbon ---
    t.goto(x - width/2, y - height*0.1)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height*0.2)
        t.left(90)
    t.end_fill()
    
    # --- Bow ---
    t.color(ribbon_color)
    t.fillcolor(ribbon_color)
    
    # Left loop
    t.goto(x - width*0.1, y + height/2)
    t.begin_fill()
    t.circle(width*0.15, 180)
    t.end_fill()
    
    # Right loop
    t.goto(x + width*0.1, y + height/2)
    t.begin_fill()
    t.circle(-width*0.15, 180)
    t.end_fill()

if __name__ == "__main__":
    screen.tracer(0)
    background()
    draw_christmas_tree()
    
    draw_snowflakes(t)
    draw_snowflakes_ground(t)

    clouds(t,6)

    x_house = 150
    y_house = -200
    width_house = 100
    draw_walls(t,x_house,y_house,width_house,50,"black")
    draw_roof(t,x_house,y_house+50, 100, "black")

    draw_circle(t,-150,-100,25,"white",True)
    draw_circle(t,-146,-78,20,"white",True)
    draw_hat(t,-132.5,-95)  
    
    margin(800,600,"#42220E")
    screen.update()
    screen.exitonclick()

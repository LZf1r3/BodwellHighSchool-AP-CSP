import random as r
import turtle
from itertools import cycle
import math
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
    t.pensize(0.5)
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
    t.pensize(1)
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

def draw_set_of_ornaments(t, x, y, spacing, count):
    colors = ["red", "blue", "gold", "silver", "green"]
    for i in range(count):
        ornament_x = x + i * spacing
        ornament_y = y + r.randint(-10, 10)  # slight vertical randomness
        color = r.choice(colors)
        draw_circle(t, ornament_x, ornament_y, 7, color)
    
def clouds(t,number):
    for _ in range(number):
        draw_fuzzy_cloud(t,r.randint(-400,400),r.randint(150,200))

def draw_centered_star(t,x,y,size):
    
    draw_circle(t,x+25,y-8,size/5,"#FAE628")
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color("#FFEC00")
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144) # Angle for a 5-pointed star
    t.end_fill()
    t.color("black")

def draw_snowman(t,x,y):
    # Bottom circle
    draw_circle(t, x, y, 20, "white")
    # Middle circle
    draw_circle(t, x, y + 30, 15, "white")
    # Head circle
    draw_circle(t, x, y + 50, 10, "white")

    # Eyes
    draw_circle(t, x - 4, y + 55, 2, "black")
    draw_circle(t, x + 4, y + 55, 2, "black")

    # Nose (carrot)
    t.penup()
    t.goto(x, y + 50)
    t.pendown()
    t.color("orange")
    t.setheading(0)
    t.begin_fill()
    t.forward(5)
    t.left(120)
    t.forward(5)
    t.left(120)
    t.forward(5)
    t.end_fill()

    # Buttons
    for i in range(3):
        button_y = y + 20 + i * 10
        t.color("black")
        draw_circle(t, x, button_y, 2, "black")

    # Arms
    t.penup()
    t.goto(x - 15, y + 30)
    t.pendown()
    t.setheading(160)
    t.forward(20)

    t.penup()
    t.goto(x + 15, y + 30)
    t.pendown()
    t.setheading(20)
    t.forward(20)

def draw_rectangle(t, x, y, w, h, color):
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

def draw_window(t, x, y, w, h):
    draw_rectangle(t, x, y, w, h, "#C29606")  # Window frame
    t.color("black")
    t.width(2)
    # Vertical line
    t.penup()
    t.goto(x + w / 2, y)
    t.pendown()
    t.goto(x + w / 2, y + h)
    # Horizontal line
    t.penup()
    t.goto(x, y + h / 2)
    t.pendown()
    t.goto(x + w, y + h / 2)
    t.width(1)

def draw_gifts():
    """Draw Christmas presents"""
    gift_data = [
        (-370, -148, 30, 25, 'red', 'gold'),
        (-340, -155, 25, 30, '#00CED1', 'white'),
        (-310, -150, 28, 22, 'green', 'red'),
        (-280, -145, 35, 30, 'purple', 'gold')
    ]
    
    for x, y, width, height, box_color, ribbon_color in gift_data:
        # Box
        t.penup()
        t.goto(x, y)
        t.color(box_color)
        t.pendown()
        t.begin_fill()
        for _ in range(2):
            t.forward(width)
            t.left(90)
            t.forward(height)
            t.left(90)
        t.end_fill()
        
        # Ribbon
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
    t.goto(0,0)

def draw_cabin(t,x,y,width,height):
    roof_height = height * 0.5
    door_width = width * 0.2
    door_height = height * 0.4
    door_x = x + (width - door_width) / 2
    door_y = y
    chimney_width = width * 0.15
    chimney_height = height * 0.4
    chimney_x = x + width * 0.75
    chimney_y = y + height + roof_height * 0.15
    win_width = width * 0.25
    win_height = height * 0.25
    win_x = x + width * 0.1
    win_y = y + height * 0.5
    # Cabin base
    draw_rectangle(t, x, y, width, height, "#6b3f27")

    # Door
    
    draw_rectangle(t, door_x, door_y, door_width, door_height, "#3e2723")

    #chimney
    #chimney   smoke
    for i in range(5):
        smoke_x = chimney_x + chimney_width / 2 + r.randint(-10, 10)
        smoke_y = chimney_y + chimney_height + i * 15
        smoke_radius = r.randint(8, 15)
        draw_circle(t, smoke_x, smoke_y, smoke_radius, "lightgray", outline=False)
    draw_rectangle(t, chimney_x, chimney_y, chimney_width, chimney_height, "#5a3e2b")
    
    # Door knob
    draw_circle(t, door_x + door_width - 10, door_y + door_height / 2, 3, "gold")

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

    # Window
    
    draw_window(t, win_x, win_y, win_width, win_height)

    #draw window frame (cross)
    t.color("#c9a36b")
    t.width(3)
    # Outer frame
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
    # Vertical bar
    t.goto(win_x + win_width / 2, win_y)
    t.setheading(90)
    t.down()
    t.forward(win_height)
    t.up()
    # Horizontal bar
    t.goto(win_x, win_y + win_height / 2)
    t.setheading(0)
    t.down()
    t.forward(win_width)
    t.up()

    
if __name__ == "__main__":
    screen.tracer(0)
    #Sky design
    background()
    clouds(t,6)

    #Ground
    draw_rectangle_fill(t,-400,-300,800,150,"darkgreen")
    

    #Draw the cozy Christmas cabin
    draw_cabin(t, 200,-150,200,125)

    # Christmas tree
    draw_christmas_tree()
    draw_centered_star(t, -325, 140, 50)

    #Snowflakes in the sky and on the ground
    draw_snowflakes(t)
    draw_snowflakes_ground(t)

    #Gifts unde  r the tree
    draw_gifts()
    
    draw_snowman(t,-180,-150)
    #House parameters
    x_house = 150
    y_house = -200
    width_house = 100

    #House function
    
    margin(800,600,"#42220E")
    screen.update()
    screen.exitonclick()

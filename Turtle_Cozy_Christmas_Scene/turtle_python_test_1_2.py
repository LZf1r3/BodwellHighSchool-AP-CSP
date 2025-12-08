import turtle
import random

# Setup
screen = turtle.Screen()
screen.setup(width=1000, height=800)
screen.title("Cozy Christmas Scene")
screen.tracer(0)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

def draw_sky():
    """Draw dark night sky with gradient"""
    t.penup()
    t.goto(-500, 400)
    colors = ['#0a0a2e', '#16213e', '#1a1a3e']
    for i in range(800):
        t.goto(-500, 400 - i)
        color_idx = min(i // 270, len(colors) - 1)
        t.pencolor(colors[color_idx])
        t.pendown()
        t.goto(500, 400 - i)
        t.penup()

def draw_stars():
    """Draw twinkling stars"""
    t.color('white')
    for _ in range(50):
        x = random.randint(-480, 480)
        y = random.randint(100, 380)
        size = random.randint(1, 3)
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.dot(size)

def draw_snow_ground():
    """Draw snowy ground"""
    t.penup()
    t.goto(-500, -120)
    t.pendown()
    t.color('white')
    t.begin_fill()
    # Create rolling hills
    for x in range(-500, 501, 50):
        t.goto(x, -120 + random.randint(-5, 10))
    t.goto(500, -400)
    t.goto(-500, -400)
    t.goto(-500, -120)
    t.end_fill()

def draw_cabin():
    """Draw a cozy cabin"""
    # Main cabin body
    t.penup()
    t.goto(-150, -100)
    t.setheading(0)
    t.color('#8B4513')
    t.pendown()
    t.begin_fill()
    for _ in range(2):
        t.forward(180)
        t.left(90)
        t.forward(120)
        t.left(90)
    t.end_fill()
    
    # Roof
    t.penup()
    t.goto(-170, 20)
    t.color('#654321')
    t.pendown()
    t.begin_fill()
    t.goto(90, 100)
    t.goto(250, 20)
    t.goto(-170, 20)
    t.end_fill()
    
    # Snow on roof
    t.color('white')
    t.penup()
    t.goto(-160, 20)
    t.pendown()
    t.begin_fill()
    t.goto(90, 90)
    t.goto(240, 20)
    t.goto(240, 15)
    t.goto(90, 85)
    t.goto(-160, 15)
    t.end_fill()
    
    # Door
    t.penup()
    t.goto(-50, -100)
    t.color('#654321')
    t.pendown()
    t.begin_fill()
    for _ in range(2):
        t.forward(40)
        t.left(90)
        t.forward(70)
        t.left(90)
    t.end_fill()
    
    # Door knob
    t.penup()
    t.goto(-15, -65)
    t.dot(5, 'gold')
    
    # Windows
    for x_offset in [50, 110]:
        t.penup()
        t.goto(-130 + x_offset, -40)
        t.color('#FFA500')
        t.pendown()
        t.begin_fill()
        for _ in range(4):
            t.forward(35)
            t.left(90)
        t.end_fill()
        
        # Window panes
        t.color('#8B4513')
        t.width(2)
        t.penup()
        t.goto(-130 + x_offset + 17.5, -40)
        t.pendown()
        t.goto(-130 + x_offset + 17.5, -5)
        t.penup()
        t.goto(-130 + x_offset, -22.5)
        t.pendown()
        t.goto(-130 + x_offset + 35, -22.5)
        t.width(1)
    
    # Chimney
    t.penup()
    t.goto(50, 20)
    t.color('#8B4513')
    t.pendown()
    t.begin_fill()
    for _ in range(2):
        t.forward(25)
        t.left(90)
        t.forward(50)
        t.left(90)
    t.end_fill()
    
    # Smoke
    t.color('#D3D3D3')
    for i in range(5):
        t.penup()
        t.goto(60 + i * 5, 70 + i * 15)
        t.dot(10 + i * 2)

def draw_christmas_tree():
    """Draw a decorated Christmas tree"""
    # Tree trunk
    t.penup()
    t.goto(200, -100)
    t.color('#8B4513')
    t.pendown()
    t.begin_fill()
    for _ in range(2):
        t.forward(20)
        t.left(90)
        t.forward(30)
        t.left(90)
    t.end_fill()
    
    # Tree layers
    tree_colors = ['#0d5c0d', '#0e6e0e', '#0f7f0f']
    y_positions = [-70, -30, 10]
    widths = [120, 90, 60]
    
    for i, (y_pos, width) in enumerate(zip(y_positions, widths)):
        t.penup()
        t.goto(210 - width / 2, y_pos)
        t.color(tree_colors[i % len(tree_colors)])
        t.pendown()
        t.begin_fill()
        t.goto(210, y_pos + 50)
        t.goto(210 + width / 2, y_pos)
        t.goto(210 - width / 2, y_pos)
        t.end_fill()
    
    # Star on top
    t.penup()
    t.goto(210, 60)
    t.color('gold')
    for _ in range(5):
        t.pendown()
        t.forward(15)
        t.right(144)
    
    # Ornaments
    ornament_colors = ['red', 'gold', '#00CED1', 'pink']
    ornament_positions = [
        (190, -50), (230, -50), (210, -35),
        (200, -10), (220, -15),
        (205, 20), (215, 25)
    ]
    
    for x, y in ornament_positions:
        t.penup()
        t.goto(x, y)
        t.dot(8, random.choice(ornament_colors))

def draw_gifts():
    """Draw Christmas presents"""
    gift_data = [
        (-200, -100, 30, 25, 'red', 'gold'),
        (-160, -100, 25, 30, '#00CED1', 'white'),
        (-130, -100, 28, 22, 'green', 'red'),
        (280, -100, 35, 30, 'purple', 'gold')
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

def draw_falling_snow():
    """Draw snowflakes falling"""
    t.color('white')
    for _ in range(80):
        x = random.randint(-490, 490)
        y = random.randint(-100, 380)
        size = random.randint(2, 5)
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.dot(size)

# Draw scene in layers
draw_sky()

draw_stars()
draw_snow_ground()
draw_cabin()
draw_christmas_tree()
draw_gifts()
draw_falling_snow()

# Finish
screen.update()
screen.mainloop()
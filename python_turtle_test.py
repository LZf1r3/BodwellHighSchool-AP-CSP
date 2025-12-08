import turtle
from itertools import cycle

t = turtle.Turtle()

def vertical_gradient():
    start_pos = -200, 200
    end_pos = 200, -200
    start_color = 154,0,254
    end_color = 221,122,80

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

vertical_gradient()
turtle.exitonclick()
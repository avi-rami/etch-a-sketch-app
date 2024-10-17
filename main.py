from turtle import Turtle, Screen

# requirements:
# 1. W = forwards
# 2. S = Backwards
# 3. A = counter-clockwise
# 4. D = clockwise

# Note for user: to make curves, alternate between pressing a/d and w/s

pen = Turtle()
screen = Screen()

def move_forwards():
    pen.forward(10)
def move_backwards():
    pen.back(10)
def rotate_clockwise():
    current_heading = pen.heading()
    pen.setheading(current_heading+10)
def rotate_counterclockwise():
    current_heading = pen.heading()
    pen.setheading(current_heading-10)
def clear_screen():
    screen.resetscreen()

screen.listen()
# move forward
screen.onkey(key="W", fun=move_forwards)
screen.onkey(key="w", fun=move_forwards)
# move backward
screen.onkey(key="S", fun=move_backwards)
screen.onkey(key="s", fun=move_backwards)
# rotate clockwise
screen.onkey(key="A", fun=rotate_clockwise)
screen.onkey(key="a", fun=rotate_clockwise)
# rotate counterclockwise
screen.onkey(key="D", fun=rotate_clockwise)
screen.onkey(key="d", fun=rotate_clockwise)
# clear drawing
screen.onkey(key="C", fun=clear_screen)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
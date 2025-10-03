from turtle import *
from random import choice
speed(100)
x=(0, 200, 400, 600, -200, -400, -600)
y=(0, 200, 400, 600, -200, -400, -600)
# Move to starting position
def start_position():
    penup()
    goto(choice(x), choice(y))
    pendown()

def draw_square(size):
    for _ in range(4):
        forward(size)
        right(90)
        
def draw_pattern():
    colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']
    start_position()
    for i in range(36):

        pencolor(colors[i % len(colors)])
        draw_square(100)
        right(10)
    done()
draw_pattern()
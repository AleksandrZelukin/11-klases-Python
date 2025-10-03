from turtle import *
from random import choice
speed(1000)
x=(0, 100, 200, 400, -100, -200, -400)
y=(0, 100, 200, 400, -100, -200, -400)
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
    for j in range(36):
        start_position()
        for i in range(6):
            pencolor(colors[i % len(colors)])
            draw_square(100)
            right(60)
    done()
draw_pattern()
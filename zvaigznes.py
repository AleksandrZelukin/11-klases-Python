from turtle import *
from tkinter import *
setup(800, 800)
bgcolor("blue")
color("yellow")
speed(10)
fillcolor("yellow")
Button(text="Exit", command=bye).pack() 
def star():
    begin_fill()
    for i in range(5):
        forward(80)
        right(144)
    end_fill()
penup()
positions = [(-150, 150), (150, 150), (-150, -150), (150, -150)]

for pos in positions:
    goto(pos)
    star()
  
home()
star()
mainloop()
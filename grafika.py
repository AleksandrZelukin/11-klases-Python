import turtle

screen = turtle.Screen()
screen.setup(550, 550)

t = turtle.Turtle()

for i in range(4):
    t.forward(100)
    t.left(90)
t.right(90)
for i in range(4):
    t.forward(100)
    t.right(90)
t.home()   
turtle.mainloop()
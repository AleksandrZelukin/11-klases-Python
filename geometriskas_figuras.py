import turtle as t
import tkinter as tk
import random
krasa = ["red","blue","orange","green","yellow"]

a = t.Screen()
a.setup(700,800)

label1=tk.Label(text="Zīmējam ģeometriskas figūras!", font=("Helvetika",24),background="lightblue",foreground=krasa[1])
label1.place(x=150, y=5)
t.shape("turtle")

t.speed(10)
t.pensize(6)
t.bgcolor("lightblue")


def kvadrats(s=150):
    t.clear() # Notīra iepriekšējo zīmējumu
    t.color(random.choice(krasa))
    for _ in range(4):
        t.forward(s)
        t.right(90)
def daudzsturis(s=150, n=6):
    t.clear() # Notīra iepriekšējo zīmējumu
    t.color(random.choice(krasa))
    for _ in range(n):
        t.forward(s)
        t.right(360/n)
def zvaigzne(s=150):
    t.clear() # Notīra iepriekšējo zīmējumu
    t.color(random.choice(krasa))
    for _ in range(5):
        t.forward(s)
        t.right(144)
def aplis(r=70):
    t.clear() # Notīra iepriekšējo zīmējumu
    t.color(random.choice(krasa))
    t.circle(r)

btn1 = tk.Button(text="Sešstūris", command=daudzsturis,width=20, height=2)
btn1.place(x=50, y=50)

btn2 = tk.Button(text="Zvaigzne", command=zvaigzne,width=20, height=2)
btn2.place(x=200, y=50)

btn3 = tk.Button(text="Aplis", command=aplis,width=20, height=2)
btn3.place(x=350, y=50)

btn4 = tk.Button(text="Kvadrāts", command=kvadrats,width=20, height=2)
btn4.place(x=500, y=50)

btn5 = tk.Button(text="Quit", command=exit,width=85, height=2)
btn5.place(x=50, y=100)
t.mainloop()

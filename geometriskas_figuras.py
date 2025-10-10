import turtle as t
import tkinter as tk
import random
krasa = ["red","blue","orange","green","yellow"]

a = t.Screen()
a.setup(800,800)

tk.Label(text="Zīmējam ģeometriskas figūras!").pack()
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
btn2.place(x=50, y=100)

btn3 = tk.Button(text="Aplis", command=aplis,width=20, height=2)
btn3.place(x=50, y=150)

btn4 = tk.Button(text="Kvadrāts", command=kvadrats,width=20, height=2)
btn4.place(x=50, y=200)

btn5 = tk.Button(text="Quit", command=exit,width=20, height=2)
btn5.place(x=50, y=250)
# while True:
#     print("Ko vēlies zīmēt?")
#     figura = input("""Ievadi figūras nosaukumu 
#                    trijstūris - 1, 
#                    kvadrāts - 2, 
#                    piecstūris - 3, 
#                    sešstūris - 4, 
#                    zvaigzne - 5, 
#                    aplis - 6, 
#                    daudzstūris - 7, 
#                    zvaigzne_ar_apskaiti - 8): """)

#     if figura == "1":
#         daudzsturis(100, 3)
#     elif figura == "2":
#         daudzsturis(100, 4)
#     elif figura == "3":
#         daudzsturis(100, 5)
#     elif figura == "4":
#         daudzsturis(100, 6)
#     elif figura == "5":
#         zvaigzne(100)
#     elif figura == "6":
#         aplis(50)
#     elif figura == "7":
#         daudzsturis(100, 5)
#     elif figura == "8":
#         zvaigzne_ar_apskaiti(100, 5)
#     elif figura.lower() == "stop":
#         print("Beidzam zīmēt!")
#         break
#     else:
#         print("Neatpazīta figūra!")
t.mainloop()

print("Beidzam zīmēt!")
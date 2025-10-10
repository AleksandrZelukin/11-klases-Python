from turtle import *    

print("Zīmējam ģeometriskas figūras!")
shape("turtle")
color("blue")
speed(1)
pensize(3)
bgcolor("lightgreen")


def zvaigzne_ar_apskaiti(s, n):
    clear() # Notīra iepriekšējo zīmējumu
    for _ in range(n):
        forward(s)
        right(180 - 180/n)
def daudzsturis(s, n):
    clear() # Notīra iepriekšējo zīmējumu
    for _ in range(n):
        forward(s)
        right(360/n)
def zvaigzne(s):
    clear() # Notīra iepriekšējo zīmējumu
    for _ in range(5):
        forward(s)
        right(144)
def aplis(r):
    clear() # Notīra iepriekšējo zīmējumu
    circle(r)

while True:
    print("Ko vēlies zīmēt?")
    figura = input("""Ievadi figūras nosaukumu 
                   trijstūris - 1, 
                   kvadrāts - 2, 
                   piecstūris - 3, 
                   sešstūris - 4, 
                   zvaigzne - 5, 
                   aplis - 6, 
                   daudzstūris - 7, 
                   zvaigzne_ar_apskaiti - 8): """)

    if figura == "1":
        daudzsturis(100, 3)
    elif figura == "2":
        daudzsturis(100, 4)
    elif figura == "3":
        daudzsturis(100, 5)
    elif figura == "4":
        daudzsturis(100, 6)
    elif figura == "5":
        zvaigzne(100)
    elif figura == "6":
        aplis(50)
    elif figura == "7":
        daudzsturis(100, 5)
    elif figura == "8":
        zvaigzne_ar_apskaiti(100, 5)
    elif figura.lower() == "stop":
        print("Beidzam zīmēt!")
        break
    else:
        print("Neatpazīta figūra!")

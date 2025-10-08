from turtle import *    

print("Zīmējam ģeometriskas figūras!")
shape("turtle")
color("blue")
speed(1)
pensize(3)
bgcolor("lightgreen")


kvadrats = lambda s: [forward(s), right(90)] * 4
taisnsturis = lambda w, h: [forward(w), right(90), forward(h), right(90)] * 2
trijsturis = lambda s: [forward(s), right(120)] * 3
aplis = lambda r: circle(r)
zvaigzne = lambda s: [forward(s), right(144)] * 5
daudzsturis = lambda s, n: [forward(s), right(360/n)] * n
zvaigzne_ar_apskaiti = lambda s, n: [forward(s), right(180 - 180/n)] * n


while True:
    print("Ko vēlies zīmēt?")
    figura = input("Ievadi figūras nosaukumu (trijstūris, kvadrāts, piecstūris, sešstūris): ")

    if figura == "kvadrāts":
        kvadrats(100)
    elif figura == "taisnstūris":
        taisnsturis(200, 100)
    elif figura == "trijstūris":
        trijsturis(100)
    elif figura == "aplis":
        aplis(50)
    elif figura == "zvaigzne":
        zvaigzne(100)
    elif figura == "daudzstūris":
        daudzsturis(100, 5)
    elif figura == "zvaigzne_ar_apskaiti":
        zvaigzne_ar_apskaiti(100, 5)
    else:
        print("Neatpazīta figūra!")


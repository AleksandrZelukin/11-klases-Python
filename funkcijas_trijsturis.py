import math
a=int(input("Pirma mala: "))   #trijstūra malas
b=int(input("Otra mala: "))
c=int(input("Treša mala: "))
def Trijsturis (x,y,z):
    if a+b>c and a+c>b and b+c>a:
        p = (a+b+c)/2 #trijstūra perimetrs
        s=math.sqrt(p*(p-a)*(p-b)*(p-c))
        print("Trijstūra laukums: ",round (s,2))
    else:
        print("Trijstūris neekzistē!")
        
k = Trijsturis(a,b,c)
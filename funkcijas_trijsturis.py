import math
# a=int(input("Pirma mala: "))   #trijstūra malas
# b=int(input("Otra mala: "))
# c=int(input("Treša mala: "))
def Trijsturis (a,b,c):
    if a+b>c and a+c>b and b+c>a:
        p = (a+b+c)/2 #trijstūra perimetrs
        s=math.sqrt(p*(p-a)*(p-b)*(p-c))
        print("Trijstūra laukums: ",round (s,2))
    else:
        print("Trijstūris neekzistē!")
        
k = Trijsturis(12,5,13)
l = Trijsturis(1,2,3)
m = Trijsturis(7,8,9)
n = Trijsturis(3,4,5)
a = int(input("Ievadi pirmo dalībnieku skaitu: "))
b = int(input("Ievadi otro dalībnieku skaitu: "))
c = int(input("Ievadi trešo dalībnieku skaitu: "))
def vietas(a, b, c):
    if a >= b and a >= c and b >= c:
        return (a, b, c)
    elif b >= a and b >= c and a >= c:
        return (b, a, c)
    elif c >= a and c >= b and a >= b:
        return (c, a, b)
    else:
        return None
rezultats = vietas(a, b, c)
print("Dalībnieki pēc vietas:")
if rezultats:
    print(rezultats)
else:
    print("Visi dalībnieki ir vienādi.")
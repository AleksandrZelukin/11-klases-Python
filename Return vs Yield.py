def piemers():
    num =[]
    for i in range(1, 11):
        num.append(i)   
    s = "Sveiki!"
    return num,s
print(piemers())

def piemers2():
    for i in range(0, 11):
        yield i
    print( "Sveiki!")
# print(piemers2())
for i in piemers2():
    print(i)
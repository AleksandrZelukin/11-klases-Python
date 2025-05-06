def piemers():
    yield "Rīga"
    yield "Liepāja"

print(piemers())
for i in piemers():
    print(i)
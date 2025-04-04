a = {"Rīga": "Latvija", "Berlīne": "Vācija", 
     "Viļņa": "Lietuva", "Tallina": "Igaunija",
     "Helsinki": "Somija", "Oslo": "Norvēģija"}

# print(a)

a["Praha"] = "Čehija"
# print(a)
a.pop("Helsinki")
del a["Oslo"]
# print(a["Rīga"])

# for i in a:
#     print(i, a[i])

while True:
    valsts = input("Ievadi galvaspilsētu: ")
    if valsts in a:
        print(valsts,"- galvaspisēta ",a[valsts])
        break
    else:
        print("Valsts nav datu bāzē.")
        break

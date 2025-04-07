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

for i in a.keys():
    print(i, a[i])
    
for i in a.values():
    print(i)
    
for i in a.items():
    print(i[0], i[1])
    

# while True:
#     valsts = input("Ievadi galvaspilsētu: ")
#     if valsts in a:
#         print(valsts,"- galvaspisēta ",a[valsts])
#         break
#     else:
#         print("Valsts nav datu bāzē.")
#         break

a = {"Rīga": "Latvija", "Berlīne": "Vācija", 
     "Viļņa": "Lietuva", "Tallina": "Igaunija",
     "Helsinki": "Somija", "Oslo": "Norvēģija"}

print(a)

a["Praha"] = "Čehija"
print(a)
a.pop("Helsinki")
del a["Oslo"]
print(a["Rīga"])
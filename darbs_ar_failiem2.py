import json

a = {"Rīga": "Latvija", "Berlīne": "Vācija", 
     "Viļņa": "Lietuva", "Tallina": "Igaunija",
     "Helsinki": "Somija", "Oslo": "Norvēģija"}
datne = open("dati.json", "w", encoding="UTF-8")  # atver datni rakstīšanai JSON formātā
json.dump(a, datne)  # saglabā objektu datnē
datne.close()

datne = open("dati.json", "r", encoding="UTF-8")  # atver datni lasīšanai JSON formātā
b = json.load(datne)  # ielādē objektu no datnes
datne.close()
print(b)  # izvada objektu
a = open("dati_11b.txt", "a", encoding="utf-8")
print("Jaunā rinda", file=a)
a.close()

a = open("dati_11b.txt", "r", encoding="utf-8")
print(a.read())
a.close()
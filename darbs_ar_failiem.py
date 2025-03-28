a="Sveiki,Otrais!"

datne = open("dati.txt","a",encoding="UTF-8")
# datne.write(str(a))
print(a,file=datne)
datne.close()

datne = open("dati.txt","r",encoding="UTF-8")
b=datne.read()  # nolasa visu saturu
c=datne.read(2) # nolasa 2 simbolus
d=datne.readline() # nolasa rindu
print(b)
print(c)
print(d)
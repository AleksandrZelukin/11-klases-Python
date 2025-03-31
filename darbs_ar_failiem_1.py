import pickle

a = "Sveiki, Rīga!"
datne = open("dati.data", "wb")  # atver datni rakstīšanai binārā režīmā
pickle.dump(a, datne)  # saglabā objektu datnē
datne.close()

datne = open("dati.data", "rb")  # atver datni lasīšanai binārā režīmā
b = pickle.load(datne)  # ielādē objektu no datnes  
datne.close()
print(b)  # izvada objektu
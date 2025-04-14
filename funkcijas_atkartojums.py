def tristuris (a, b, c):
    """
    Funkcija nosaka, vai trijsturis ir taisnstūra, asu vai platleņķa.
    :param a: Trijstūra pirmā mala
    :param b: Trijstūra otrā mala
    :param c: Trijstūra trešā mala
    :return: Taisnstūra, asu vai platleņķa trijstūris
    """
    if a + b <= c or a + c <= b or b + c <= a:
        return "Trijstūris nav iespējams"
    if a ** 2 + b ** 2 == c ** 2:
        return "Taisnstūra trijstūris"
    elif a ** 2 + b ** 2 > c ** 2:
        return "Asu leņķu trijstūris"
    else:
        return "Platleņķu trijstūris"
    
def laukums (a, b, c):
    """
    Funkcija aprēķina trijstūra laukumu pēc Herona formulas.
    :param a: Trijstūra pirmā mala
    :param b: Trijstūra otrā mala
    :param c: Trijstūra trešā mala
    :return: Trijstūra laukums
    """
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

a1 = int(input("Ievadiet trijstūra pirmo malu: "))
b1 = int(input("Ievadiet trijstūra otro malu: "))
c1 = int(input("Ievadiet trijstūra trešo malu: "))
   
z = tristuris(a1, b1, c1)
x = laukums(a1, b1, c1)	
try:
  print(z, "ar laukumu", round(x, 2))
except:
  print("Trijstūris nav iespējams")

import json
# Tālruņu grāmatas programma, kas ļauj pievienot, noņemt, meklēt un uzskaitīt kontaktus.
datne = open("phonebook.json", "r", encoding="UTF-8")  # atver failu lasīšanai JSON formātā
phonebook = json.load(datne)  # ielādē objektu no faila

# phonebook = {} 

def add_contact(name, phone_number):
    """Pievieno kontaktu tālruņu grāmatai."""
    phonebook[name] = phone_number
    print(f"Kontakts {name} pievienots ar tālruņa numuru {phone_number}.")
    
    
def remove_contact(name):
    """Noņem kontaktu no tālruņu grāmatas."""
    if name in phonebook:
        del phonebook[name]
        print(f"Kontakts {name} tika noņemts.")
    else:
        print(f"Kontakts {name} netika atrasts.")
        
def search_contact(name):
    """Meklē kontaktu tālruņu grāmatā."""
    if name in phonebook:
        print(f"Kontakts {name} atrasts ar tālruņa numuru {phonebook[name]}.")
    else:
        print(f"Kontakts {name} netika atrasts.")
        
def list_contacts():
    """Uzskaita visus kontaktus tālruņu grāmatā."""
    if phonebook:
        print("Tālruņu grāmatas kontakti:")
        for name, phone_number in phonebook.items():
            print(f"{name}: {phone_number}")
    else:
        print("Tālruņu grāmata ir tukša.")
        
def main():
    """Galvenā funkcija, lai palaistu tālruņu grāmatas programmu."""
    while True:
        print("\nTālruņu grāmatas izvēlne:")
        print("1. Pievienot kontaktu")
        print("2. Noņemt kontaktu")
        print("3. Meklēt kontaktu")
        print("4. Parādīt visus kontaktus")
        print("5. Iziet")
        
        choice = input("Ievadi savu izvēli (1-5): ")
        
        if choice == '1':
            name = input("Ievadi kontakta vārdu: ")
            phone_number = input("Ievadi tālruņa numuru: ")
            add_contact(name, phone_number)
            
        elif choice == '2':
            name = input("Ievadi kontakta vārdu, ko noņemt: ")
            remove_contact(name)
            
        elif choice == '3':
            name = input("Ievadi kontakta vārdu meklēšanai: ")
            search_contact(name)
            
        elif choice == '4':
            list_contacts()
            
        elif choice == '5':
            print("Iziet no tālruņu grāmatas.")
            datne = open("phonebook.json", "w", encoding="UTF-8")  # atver failu rakstīšanai JSON formātā
            json.dump(phonebook, datne)  # saglabā objektu failā
            datne.close()   
            break
            
        else:
            print("Nederīga izvēle. Mēģini vēlreiz.")
            
a = main()
print(a)
datne.close()  # aizver failu
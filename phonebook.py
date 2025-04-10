#https://sparkbyexamples.com/python/convert-json-to-dictionary-in-python/
import json
# Phonebook program that allows adding, removing, searching, and listing contacts.
datne = open("phonebook.json", "r", encoding="UTF-8")  # atver datni lasīšanai JSON formātā
phonebook = json.load(datne)  # ielādē objektu no datnes

# phonebook = {} 

def add_contact(name, phone_number):
    """Add a contact to the phonebook."""
    phonebook[name] = phone_number
    # atver datni rakstīšanai JSON formātā
    datne = open("phonebook.json", "w", encoding="UTF-8")
    json.dump(phonebook, datne)  # saglabā objektu datnē
    datne.close() 
    print(f"Contact {name} added with phone number {phone_number}.")
    
    
def remove_contact(name):
    """Remove a contact from the phonebook."""
    if name in phonebook:
        del phonebook[name]
        # atver datni rakstīšanai JSON formātā
        datne = open("phonebook.json", "w", encoding="UTF-8")
        json.dump(phonebook, datne)  # saglabā objektu datnē
        datne.close() 
        print(f"Contact {name} removed.")
    else:
        print(f"Contact {name} not found.")
        
def search_contact(name):
    """Search for a contact in the phonebook."""
    if name in phonebook:
        print(f"Contact {name} found with phone number {phonebook[name]}.")
    else:
        print(f"Contact {name} not found.")
        
def list_contacts():
    """List all contacts in the phonebook."""
    if phonebook:
        print("Phonebook contacts:")
        for name, phone_number in phonebook.items():
            print(f"{name}: {phone_number}")
    else:
        print("Phonebook is empty.")
        
def main():
    """Main function to run the phonebook program."""
    while True:
        print("\nPhonebook Menu:")
        print("1. Add contact")
        print("2. Remove contact")
        print("3. Search contact")
        print("4. List contacts")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            name = input("Enter contact name: ")
            phone_number = input("Enter phone number: ")
            add_contact(name, phone_number)
            
        elif choice == '2':
            name = input("Enter contact name to remove: ")
            remove_contact(name)
            
        elif choice == '3':
            name = input("Enter contact name to search: ")
            search_contact(name)
            
        elif choice == '4':
  
            list_contacts()
            
        elif choice == '5':
            print("Exiting phonebook.")
            break
            
        else:
            print("Invalid choice. Please try again.")
            
a=main()
print(a)
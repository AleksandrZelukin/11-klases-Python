from tkinter import *
logs=Tk()
logs.geometry("400x400")
logs.title("Trijstura kalkulators")
lab1 = Label(text="Ievadiet malas garumus")
lab1.place(x=30,y=10)


# a = int(input("Mala a: "))	# Ievada skaitli a
# b = int(input("Mala b: "))	# Ievada skaitli b	
# c = int(input("Mala c: "))	# Ievada skaitli c 

# if a+b>c and a+c>b and b+c>a:	# Ja izpildas šis nosacījums
#     print("Trijstūris ir iespējams")	# Izvada, ka trijstūris ir iespējams
#     s = (a+b+c)/2	# Aprēķina pusperimetru
#     laukums = round(((s*(s-a)*(s-b)*(s-c))**0.5),2)	# Aprēķina laukumu  pēc Herona formulas
#     print(f"Trijstura laukums ir {laukums}")	# Izvada laukumu
# else:
#     print("Trijstūris nav iespējams")    # Izvada, ka trijstūris nav iespējams
    

num1 = Entry(width=10)
num1.insert(0,"Malas a")
num1.place(x=40,y=30)

num2 = Entry(width=10)
num2.insert(0,"Malas b")
num2.place(x=100,y=30)

num3 = Entry(width=10)
num3.insert(0,"Malas c")
num3.place(x=160,y=30)  
def s():
    a = int(num1.get())
    b = int(num2.get())
    c = int(num3.get())
    if a+b>c and a+c>b and b+c>a:
        print("Trijstūris ir iespējams")
        s = (a+b+c)/2
        # laukums = round(((s*(s-a)*(s-b)*(s-c))**0.5),2)
        z = ("Trijstura laukums ir:")
        laukums = round(((s*(s-a)*(s-b)*(s-c))**0.5),2)
        z2.configure(text = z)
    else:
        laukums = ("Trijstūris nav iespējams")
    rezultats.configure(text = laukums)
    
    
btn1 = Button(text="Aprēķināt",command=s)
btn1.place(x=220,y=30) 
z2 = Label(font=("Arial", 24))
z2.place(x=10,y=60)   
rezultats = Label(font=("Arial", 24))
rezultats.place(x=10,y=120)
logs.mainloop()  
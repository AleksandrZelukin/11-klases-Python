from tkinter import *
logs=Tk()
logs.geometry("600x400")
logs.title("Trijstura kalkulators")
lab = Label(text="Ievadiet trijstura malas garumus",font=("Arial", 18))
lab.place(relx=.3,rely=.02)

lab1 = Label(text="a:")
lab1.place(relx=.1,rely=.2)
num1 = Entry(width=10)
num1.insert(0,"")
num1.place(relx=.2,rely=.2)

lab2 = Label(text="b:")
lab2.place(relx=.1,rely=.3)
num2 = Entry(width=10)
num2.insert(0,"")
num2.place(relx=.2,rely=.3)

lab3 = Label(text="c:")
lab3.place(relx=.1,rely=.4)
num3 = Entry(width=10)
num3.insert(0,"")
num3.place(relx=.2,rely=.4)  

def s():
    a = int(num1.get())
    b = int(num2.get())
    c = int(num3.get())
    s = (a+b+c)/2
    if a+b>c and a+c>b and b+c>a:
        trijsturis = ("Trijstura laukums ir:")
        rezultats1.configure(text = trijsturis)
        laukums = round(((s*(s-a)*(s-b)*(s-c))**0.5),2)
        rezultats2.configure(text = laukums)
    else:
        trijsturis = ("Trijsturis nav iespējams")
        rezultats1.configure(text = trijsturis)
        rezultats2.configure(text = "")
        laukums = ""
        rezultats2.configure(text = laukums)
        return
    return
     
btn1 = Button(text="Aprēķināt",bg="green",fg="lightblue",command=s)
btn1.place(relx=.3,rely=.5) 
trijsturis = Label(font=("Arial", 18))
trijsturis.place(relx=.2,rely=.5)   
rezultats1 = Label(font=("Arial", 18))
rezultats1.place(relx=.2,rely=.6)
rezultats2 = Label(font=("Arial", 18))
rezultats2.place(relx=.2,rely=.7)
laukums = Label(font=("Arial", 18))
laukums.place(relx=.2,rely=.8)
btn2 = Button(text="Iziet",width=10,bg="red",fg="lightblue",command=logs.quit)
btn2.place(relx=.6,rely=.5)
logs.mainloop()  
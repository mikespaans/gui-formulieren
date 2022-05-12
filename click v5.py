import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import DISABLED
from tkinter import NORMAL

window = tk.Tk()
window.title("Clicker")
window.geometry("600x300")
TextNumber = 0

Checkbutton_Var = tk.StringVar(value=0)

def CheckboxAangevinkt():
    StateChecken = Checkbutton_Var.get()
    if StateChecken == "1":
        if LaatstOmhoogOmlaag == True:
            window.after(200, Omhoog)
            window.after(200, CheckboxAangevinkt)
        else:
            window.after(200, Omlaag)
            window.after(200, CheckboxAangevinkt)
    else:
        return 

checkbox = tk.Checkbutton(
    window,
    text="<checkbox label>",
    variable=Checkbutton_Var,
    state=DISABLED,
    command=CheckboxAangevinkt,
    onvalue=1,
    offvalue=0
)
checkbox.pack()




Number = 0
def Omhoog(Event = False):
    global Number
    global LaatstOmhoogOmlaag
    global TextNumber
    Number = TextNumber
    Number += 1
    TextNumber = tk.IntVar(value= Number) 
    TextNumber = TextNumber.get()
    box1.configure(text= TextNumber)
    Achtergrond()
    LaatstOmhoogOmlaag = True
    checkbox.configure(state="normal")
    return TextNumber

def Omlaag(Event = False):
    global Number
    global LaatstOmhoogOmlaag
    global TextNumber
    Number = TextNumber
    Number -= 1
    TextNumber = tk.IntVar(value= Number) 
    TextNumber = TextNumber.get()
    box1.configure(text= TextNumber)
    Achtergrond()
    LaatstOmhoogOmlaag = False
    checkbox.configure(state="normal")
    return TextNumber

def Achtergrond(Event = False):
    if Number == 0:
        box1.configure(background="grey")
        window.configure(background="grey")
    elif Number > 0:
        box1.configure(background="green")
        window.configure(background="green")
    else:
        box1.configure(background="red")
        window.configure(background="red")

def KleurVeranderen(Event = False):
    window.configure(background="yellow")
    box1.configure(background="yellow")
    box1.bind('<Leave>', Achtergrond)

def DubbelKlik(Event = False):
    global TextNumber
    if LaatstOmhoogOmlaag == True:
        TextNumber *= 3
        box1.configure(text= TextNumber)
    else:
        TextNumber /= 3
        box1.configure(text= TextNumber)

box1 = tk.Label(
    window,
    text= 0,
    background="grey"
)
window.configure(background="grey")
button = tk.Button(text="Up", command= Omhoog)
button.pack(padx=10, pady=10)
box1.bind('<Enter>', KleurVeranderen)

box1.pack(
    ipadx=50,
    ipady=30,
    fill="both"
)

Button2 = tk.Button(text="Down", command=Omlaag)
Button2.pack(padx=100, pady=30)

button.bind('<Double-Button>', DubbelKlik)
Button2.bind('<Double-Button>', DubbelKlik)

window.bind('<Up>', Omhoog)
window.bind("+", Omhoog)

window.bind("<Down>", Omlaag)
window.bind("-", Omlaag)

window.bind("<space>", DubbelKlik)
window.mainloop()
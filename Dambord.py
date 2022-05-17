import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("Dambord")
window.geometry("500x500")

for x in range (11):
    window.rowconfigure(x)
    window.columnconfigure(x)

Kleur = "black"

for y in range(10):
    for i in range (0,10):
        box1 = Frame(window, background=Kleur, width=50, height=50)
        box1.grid(column=i, row=y)
        if Kleur == "black":
            Kleur = "white"
        else:
            Kleur = "black"
    if Kleur == "black":
        Kleur = "white"
    else:
        Kleur = "black"

window.mainloop()
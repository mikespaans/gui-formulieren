import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from calendar import month_name
import datetime
from datetime import date

window = tk.Tk()
window.title("Days by date calculator")
window.geometry("400x200")

box1 = tk.Label(
    window,
    text="Date: ",
    font=(100)

    )
box1.pack()


def DagenUitrekenen():
    Tellen = 0
    Doorgaan = True
    NieuwJaar = selected_year.get()
    NieuwMaand = selected_month.get()
    NieuweDag = selected_day.get()
    while Doorgaan == True:
        if NieuwMaand == month_name[Tellen][0:3]:
            Doorgaan = False
            Tellen -= 1
        Tellen += 1
    VandaagList = date(Tijd.year, Tijd.month, Tijd.day)
    IngevuldeList = date(int(NieuwJaar), int(Tellen), int(NieuweDag))
    delta = IngevuldeList - VandaagList

    print (delta.days)
    if delta.days > 0:
        showinfo(" ","Dit is "+str(delta.days)+" dagen in de toekomst")
    elif delta.days == 0:
        showinfo(" ", "Dit is vandaag")
    else:
        Dagen = delta.days * 2
        DagenGeleden = delta.days - Dagen
        showinfo(" ", "Dit is "+str(DagenGeleden)+" dagen geleden")


Days = []
for i in range(1,32):
    Days.append(str(i))

Tijd = datetime.datetime.today()

selected_day = tk.StringVar(value= Tijd.day)
day_cb = ttk.Combobox(window, textvariable=selected_day)

# get first 3 letters of every year name
day_cb['values'] = [Days[m] for m in range(31)]

# place the widget
day_cb.pack(padx=5, pady=5)





Maand = Tijd.month

selected_month = tk.StringVar(value=month_name[Maand][0:3])
month_cb = ttk.Combobox(window, textvariable=selected_month)

# get first 3 letters of every month name
month_cb['values'] = [month_name[m][0:3] for m in range(1, 13)]

# place the widget
month_cb.pack(padx=5, pady=5)







selected_year = tk.StringVar(value=Tijd.year)
year_cb = ttk.Entry(window, textvariable=selected_year)

# place the widget
year_cb.pack(padx=5, pady=5)


Button = tk.Button(text="go", command=DagenUitrekenen)
Button.pack(padx=5, pady=5)



window.mainloop()
import tkinter as tk
from tkinter import ttk
from functools import partial
from calendar import month_name
from tkinter.messagebox import showerror
import random


window = tk.Tk()
window.title("registratie formulier")
window.geometry("400x500")
window.configure(background="lightgrey")


def E_sportsLabel():
    EsportsLabel = tk.Label(text="E-sports", font=("Courier", 30), background="lightgrey")
    EsportsLabel.place(x=200, y= 50)

E_sportsLabel()

def Mr_Or_MRs():
    TitleLabel = tk.Label(window, text="Title", background="lightgrey")
    TitleLabel.place(x = 10, y= 10)

    MR_MRs = tk.StringVar()
    MRCombobox = ttk.Combobox(window, textvariable=MR_MRs, state="readonly")
    MRCombobox["values"] = ["Mr", "Mrs"]
    MRCombobox.place(x= 14, y= 30)
    return MR_MRs

# Mr_Or_MRs()

def First_Name():
    FirstNameLabel = tk.Label(window, text="First Name", background="lightgrey")
    FirstNameLabel.place(x= 10, y= 60)

    VoorNaam = tk.StringVar()
    FirstName = tk.Entry(window, textvariable=VoorNaam)
    FirstName.place(x=14, y=80, width=142)
    return VoorNaam
    
# First_Name()


def Last_Name():
    LastNameLabel = tk.Label(window, text="Last Name", background="lightgrey")
    LastNameLabel.place(x=10, y= 110)

    AchterNaam = tk.StringVar()
    LastName = tk.Entry(window, textvariable=AchterNaam)
    LastName.place(x=14, y=130, width=142)
    return AchterNaam

# Last_Name()


def Date_OF_Birth():
    global GeboorteJaar
    global selected_month
    global selected_day
    DateBirthLabel = tk.Label(window, text="Date of Birth", background="lightgrey")
    DateBirthLabel.place(x=10, y=160)

    # jaren
    GeboorteJaar = tk.StringVar(value=0)
    BirthYear = tk.Entry(window, textvariable=GeboorteJaar)
    BirthYear.place(x=108, y=180, width=44)

    # maanden
    selected_month = tk.StringVar()
    month_cb = ttk.Combobox(window, textvariable=selected_month, state="readonly")
    month_cb['values'] = [month_name[m][0:3] for m in range(1, 13)]
    month_cb.place(x=56, y=180, width=50)

    # dagen
    Days = []
    for i in range(1,32):
        Days.append(str(i))
    selected_day = tk.StringVar()
    day_cb = ttk.Combobox(window, textvariable=selected_day, state="readonly")
    day_cb['values'] = [Days[m] for m in range(31)]
    day_cb.place(x=14, y=180, width=40)


Date_OF_Birth()

def Phone_Number():
    TelefoonLabel = tk.Label(window, text="phone", background="lightgrey")
    TelefoonLabel.place(x=10, y=210)

    TelefoonNummer = tk.StringVar(value="06-")
    TelefoonEntry = tk.Entry(window, textvariable=TelefoonNummer)
    TelefoonEntry.place(x=14, y=230, width=142)
    return TelefoonNummer

# Phone_Number()


def FormulierChecken(MR_MRs, VoorNaam, AchterNaam, TelefoonNummer):
    Title = MR_MRs.get()
    FirstName = VoorNaam.get()
    LastName = AchterNaam.get()
    BirthYear = GeboorteJaar.get()
    BirthMonth = selected_month.get()
    BirthDate = selected_day.get()
    PhoneNumber = TelefoonNummer.get()

    if len(Title) and len(FirstName) and len(LastName) and len(BirthDate) and len(BirthMonth) >= 1 and int(BirthYear) > 1950 and int(BirthYear) < 2020 and len(PhoneNumber) == 11:
        window.destroy()      
        NieuweWindow(Title, FirstName, LastName, PhoneNumber, BirthDate, BirthMonth, BirthYear)
    else:
        showerror("Not valid", "Information not valid, please check your information and try again.")
  


def CheckButton():
    FormulierCheck = tk.Button(text="check formulier", command=partial(FormulierChecken, Mr_Or_MRs(), First_Name(), Last_Name(), Phone_Number()))
    FormulierCheck.place(x = 100, y=400 )


def NieuweWindow(MR_MRsTitel, VoorNaam, AchterNaam, TelefoonNummer, GeboorteDag, GeboorteMaand, GeboorteJaar):
    Window = tk.Tk()
    Window.title("registratie formulier")
    Window.geometry("400x500")
    Window.configure(background="lightgrey")


    box1 = tk.Label(Window, background="lightgrey",text=MR_MRsTitel +" "+ VoorNaam +" "+ AchterNaam)
    box1.place(x = 10, y = 10)

    box2 = tk.Label(Window, background="lightgrey",text=GeboorteJaar +" "+ GeboorteMaand +" "+ GeboorteJaar)
    box2.place(x = 10, y = 40)

    box3 = tk.Label(Window, background="lightgrey",text=TelefoonNummer)
    box3.place(x = 10, y = 70)

    box4 = tk.Label(Window, background="lightgrey",text="unique registration code:")
    box4.place(x = 10, y = 100)

    RegistratieCode = ""
    for i in range(10):
        RandomCijfer = random.randint(0,9)
        RegistratieCode += str(RandomCijfer)

    box5 = tk.Label(Window, background="lightgrey",text=RegistratieCode)
    box5.place(x = 150, y = 100)

CheckButton()




window.mainloop()
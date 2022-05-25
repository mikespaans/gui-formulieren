import tkinter as tk
from tkinter.messagebox import showerror
from tkinter.messagebox import askyesno
from tkinter.messagebox import showinfo
import random
import string

window = tk.Tk()
window.title("raad het woord - speler 1")
window.geometry("500x300")

def WoordInStellen():
    global NieuwWoord
    global Score
    Label1.destroy()
    Label2.destroy()
    Woord_Vragen.destroy()
    StelWoordIn.destroy()
    
    NieuwWoord = IngeVuldeWoord.get()
    if len(NieuwWoord) >= 4 and len(NieuwWoord) <= 7:
        window.title("raad het woord - speler 2")
        Score = len(NieuwWoord) * len(NieuwWoord)
        LettersInstellen(NieuwWoord)
    else:
        showerror(" ", "het woord moet tussen de 4 en 7 letters zijn. ")
        WoordVragen()


def WoordVragen():
    global Score
    Score = 0
    
    global Label1
    Label1 = tk.Label(text= "Vul een woord in", font=20)
    Label1.pack(padx=20, pady=20)

    global IngeVuldeWoord
    global Woord_Vragen
    IngeVuldeWoord = tk.StringVar()
    Woord_Vragen = tk.Entry(textvariable=IngeVuldeWoord)
    Woord_Vragen.pack()

    global Label2
    Label2 = tk.Label(text= "(4 tot 7 letters)")
    Label2.pack(padx=5, pady=5)

    global StelWoordIn
    StelWoordIn = tk.Button(text="Stel woord in", command=WoordInStellen)
    StelWoordIn.pack(padx=30, pady=60)


def LettersInstellen(Woord):
    global VariableList
    global SpinboxList
    global ButtonGok

    Eerste_Letter = tk.StringVar()
    Tweede_Letter = tk.StringVar()
    Derde_Letter = tk.StringVar()
    Vierde_Letter = tk.StringVar()
    Vijfde_Letter = tk.StringVar()
    Zesde_Letter = tk.StringVar()
    Zevende_Letter = tk.StringVar()

    Spinbox1 = False
    Spinbox2 = False
    Spinbox3 = False
    Spinbox4 = False
    Spinbox5 = False
    Spinbox6 = False
    Spinbox7 = False

    VariableList = [Eerste_Letter, Tweede_Letter, Derde_Letter, Vierde_Letter, Vijfde_Letter, Zesde_Letter, Zevende_Letter]
    SpinboxList = [Spinbox1, Spinbox2, Spinbox3, Spinbox4, Spinbox5, Spinbox6, Spinbox7]

    Tellen = 0
    for i in Woord:
        RandomList = []
        for x in range(4):
            RandomLetter = random.choice(string.ascii_lowercase)
            RandomList.append(RandomLetter)
        RandomList.append(i)
        SpinboxList[Tellen] = tk.Spinbox(
            window,
            textvariable=VariableList[Tellen],
            state="readonly",
            values=RandomList,
            wrap=True
        )

        SpinboxList[Tellen].pack(pady=1, padx=1, )
        Tellen += 1

    ButtonGok = tk.Button(text="Doe een gok", command=WoordChecken)
    ButtonGok.pack(padx=5, pady=5) 

def WoordChecken():
    global Score
    NieuweWoord1 = VariableList[0].get()
    NieuweWoord2 = VariableList[1].get()
    NieuweWoord3 = VariableList[2].get() 
    NieuweWoord4 = VariableList[3].get()
    NieuweWoord5 = VariableList[4].get()
    NieuweWoord6 = VariableList[5].get()
    NieuweWoord7 = VariableList[6].get()
    TotaalWoord = NieuweWoord1+NieuweWoord2+NieuweWoord3+NieuweWoord4+NieuweWoord5+NieuweWoord6+NieuweWoord7

    if TotaalWoord == NieuwWoord:
        OpnieuwSpelen = askyesno("Woord geraden", "Gefeliciteerd, Je hebt het woord geraden. Je score is: "+str(Score)+"  Wil je nog een keer spelen?")
        if OpnieuwSpelen:
            for i in range(len(NieuwWoord)):
                SpinboxList[i].destroy()
            ButtonGok.destroy()
            WoordVragen()
        else:
            window.destroy()
    else:
        LetterTellen = 0
        GoedeLetter = 0
        NietOpnieuw = 0
        for i in TotaalWoord:
            if i != NieuwWoord[LetterTellen]:
                Score -= 2
                if Score <= 0 and NietOpnieuw == 0:
                    showinfo("Geen punten", "Helaas, je punten zijn op. Het spel is afgelopen.")
                    window.destroy()
                    NietOpnieuw += 1
                    
            else:
                GoedeLetter += 1
            LetterTellen += 1

        if NietOpnieuw == 0:
            showinfo("helaas", "Helaas er zijn "+str(GoedeLetter)+" letters goed")
WoordVragen()



window.mainloop()
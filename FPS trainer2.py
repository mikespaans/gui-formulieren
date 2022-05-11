import tkinter as tk
from tkinter.messagebox import askyesno
from tkinter.messagebox import showinfo
import random

window = tk.Tk()
window.title("FPS Trainer")
window.geometry("600x400")
window.configure(background="lightgrey")

box3 = tk.Frame(window)
box3.place(y=100, x=150, width= 300, height= 30)
def TijdVragen():
    global textbox
    Tijd= tk.StringVar(value=20)

    textbox = tk.Entry(box3, textvariable=Tijd)
    textbox.pack(fill="both", expand=True)

   
    return textbox


Timer = tk.Label(
    window,
    background="black",
    fg="white",
    text="Time remaining: 20""                                                                  points :0"
)

Timer.pack(
    ipadx=50,
    ipady=15,
    fill="both"
)


AflopendeTijd = TijdVragen()
# print (AflopendeTijd)
Punten = 0
BijkomendePunten = 0

def StartKnop():
    global NieuweTijd
    IngeVuldeTijd = AflopendeTijd.get()
    NieuweTijd = int(IngeVuldeTijd)
    print (NieuweTijd)
    textbox.destroy()
    # print (AflopendeTijd)
    box3.configure(background="lightgrey")
    OpdrachtKiezen()
    window.after(1000, TimeFunctie)

def StartKnop2():
    global Punten
    global BijkomendePunten
    global NieuweTijd
    
    IngeVuldeTijd = AflopendeTijd.get()
    NieuweTijd = int(IngeVuldeTijd)
    print (NieuweTijd)
    textbox.destroy()
    Punten = 0
    BijkomendePunten = 0
    box2.destroy()
    OpdrachtKiezen()

def OpdrachtKiezen(event = False):
    global Punten
    global BijkomendePunten
    window.unbind("a")
    window.unbind("w")
    window.unbind("s")
    window.unbind("d")
    window.unbind("<space>")
    window.unbind("<Button>")
    window.unbind("<Double-Button>")
    window.unbind("<Triple-Button>")
    Punten += BijkomendePunten 
    OpdrachtList = [W_ToetsFunctie, A_ToetsFunctie, S_ToetsFunctie, D_ToetsFunctie, Spatie_ToetsFunctie, EnkeleKlik_Functie, DubbelKlik_Functie, DrieDubbelKlik_Functie]
    box1.destroy()
    Timer.configure(text="Time remaining: " + str(NieuweTijd)+"                                                                  points :" +str(Punten))
    RandomOpdracht = random.choice(OpdrachtList)
    OpdrachtPositieX = random.randint(0,525)
    OpdrachtPositieY = random.randint(51,345)
    RandomOpdracht(OpdrachtPositieX, OpdrachtPositieY)



def TimeFunctie():
    global NieuweTijd
    NieuweTijd -= 1
    Timer.configure(text="Time remaining: " + str(NieuweTijd)+"                                                                  points :" +str(Punten))
    if NieuweTijd == 0:
        box1.destroy()
        Answer = askyesno("Retry", "Congratulations you have "+str(Punten)+ " points, wanna play again")
        if Answer == False:
            window.destroy()
        else:
            global box2
            global AflopendeTijd
            AflopendeTijd = TijdVragen()
            box2 = tk.Button(text="Press to start", command=StartKnop2)
            box2.pack(pady=150, padx=10)
            
    window.after(1000, TimeFunctie)

def W_ToetsFunctie(Xpositie, YPositie):
    global box1
    global BijkomendePunten
    BijkomendePunten = 2
    box1 = tk.Label(
        window,
        text="Press: w"
    )
    box1.place(
        x=Xpositie,
        y=YPositie,
        width=70,
        height=70
    )
    window.bind("w", OpdrachtKiezen)
    

def A_ToetsFunctie(Xpositie, YPositie):
    global box1
    global BijkomendePunten
    BijkomendePunten = 2
    box1 = tk.Label(
        window,
        text="Press: a"
    )
    box1.place(
        x=Xpositie,
        y=YPositie,
        width=70,
        height=70
    )
    window.bind("a", OpdrachtKiezen)

def S_ToetsFunctie(Xpositie, YPositie):
    global box1
    global BijkomendePunten
    BijkomendePunten = 2
    box1 = tk.Label(
        window,
        text="Press: s"
    )
    box1.place(
        x=Xpositie,
        y=YPositie,
        width=70,
        height=70
    )
    window.bind("s", OpdrachtKiezen)

def D_ToetsFunctie(Xpositie, YPositie):
    global box1
    global BijkomendePunten
    BijkomendePunten = 2
    box1 = tk.Label(
        window,
        text="Press: d"
    )
    box1.place(
        x=Xpositie,
        y=YPositie,
        width=70,
        height=70
    )
    window.bind("d", OpdrachtKiezen)

def Spatie_ToetsFunctie(Xpositie, YPositie):
    global box1
    global BijkomendePunten
    BijkomendePunten = 2
    box1 = tk.Label(
        window,
        text="Press: Space"
    )
    box1.place(
        x=Xpositie,
        y=YPositie,
        width=70,
        height=70
    )
    window.bind("<space>", OpdrachtKiezen)

def EnkeleKlik_Functie(Xpositie, YPositie):
    global box1
    global BijkomendePunten
    BijkomendePunten = 1
    box1 = tk.Label(
        window,
        text="Single Click"
    )
    box1.place(
        x=Xpositie,
        y=YPositie,
        width=70,
        height=70
    )
    window.bind("<Button>", OpdrachtKiezen)

def DubbelKlik_Functie(Xpositie, YPositie):
    global box1
    global BijkomendePunten
    BijkomendePunten = 1
    box1 = tk.Label(
        window,
        text="Double Click"
    )
    box1.place(
        x=Xpositie,
        y=YPositie,
        width=70,
        height=70
    )
    window.bind("<Double-Button>", OpdrachtKiezen)

def DrieDubbelKlik_Functie(Xpositie, YPositie):
    global box1
    global BijkomendePunten
    BijkomendePunten = 1
    box1 = tk.Label(
        window,
        text="Triple Click"
    )
    box1.place(
        x=Xpositie,
        y=YPositie,
        width=70,
        height=70
    )
    window.bind("<Triple-Button>", OpdrachtKiezen)

# TijdVragen()
box1 = tk.Button(text="Press to start", command=StartKnop)
box1.pack(pady=150, padx=10)

window.mainloop()
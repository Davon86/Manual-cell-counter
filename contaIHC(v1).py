from cProfile import label
from ctypes import alignment
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import keyboard

#impostare i tasti personalizzabili e il salvataggio delle impostazioni



tastoA = "a"
tastoB = "b"
tastoEND = "esc"

countA = 0
countB = 0

desc_parziale = "Conta totale delle cellule: "

window = tk.Tk()
window.geometry("400x200")
window.title("Conta cellule")
window.grid_columnconfigure(0, weight=1)
window.resizable(False, False)

def incrementoA():
    global countA
    countA += 1
    print("Contatore POS: " + str(countA))


def incrementoB():
    global countB
    countB += 1
    print("Contatore NEG: " + str(countB))

def conta():
    global tastoA
    global tastoB
    global tastoEND
    global pop
    global desc_parziale
    global countA
    global countB
    global text_risultato

    countA = 0
    countB = 0

    tempA = 0
    tempB = 0

    text_risultato = tk.Label(window, text=("Positività: \nTotale cellule contate: " + str(countA+countB)), fg="black",font=("Helvetica",16))
    text_risultato.grid(row=12, column=0, pady=10)

    pop = Toplevel(window)
    pop.title("Conta in corso")
    pop.geometry("300x300")
#    messagebox.showinfo("Conta in corso", str(tastoA) + " -> cellule positive\n" + str(tastoB) + " -> cellule negative\n" + str(tastoEND) + " -> termina conta")
    pop_descrizione = Label(pop, text= "Premi: [ " + str(tastoA) + " ] per le cellule positive\nPremi: [ " + str(tastoB) + " ] per le cellule negative", font=(10))
    pop_descrizione.grid(row= 0, padx=20)
    pop_parziale = Label(pop, text= desc_parziale + str(countA + countB), font=(10))
    pop_parziale.grid(row= 1, padx=20, pady=50)
    pop_descrizione = Label(pop, text= "Premi: [ " + str(tastoEND) + " ] per terminare la conta", font=(10))
    pop_descrizione.grid(row = 3, padx=20)
    
    pop.update()
    
    while True: 
        keyboardTEMP = keyboard.read_event(suppress=False)
        if keyboardTEMP.event_type == keyboard.KEY_DOWN and keyboardTEMP.name == tastoA and tempA == 0:
            incrementoA() 
            tempA = 1
        if keyboardTEMP.event_type == keyboard.KEY_DOWN and keyboardTEMP.name == tastoB and tempB == 0:
            incrementoB()
            tempB = 1
        if keyboardTEMP.event_type == keyboard.KEY_UP and keyboardTEMP.name == tastoA and tempA == 1:
            tempA = 0
        if keyboardTEMP.event_type == keyboard.KEY_UP and keyboardTEMP.name == tastoB and tempB == 1:
            tempB = 0
        if keyboardTEMP.event_type == keyboard.KEY_DOWN and keyboardTEMP.name == tastoEND:
            print("premuto tasto END")
            pop.destroy()
            risultato()
            window.update()
            break
        pop_parziale = Label(pop, text= desc_parziale + str(countA + countB), font=(10))
        pop_parziale.grid(row= 1, padx=20, pady=50)
        pop.update()
        window.update()

def risultato():
    global text_risultato
    text_risultato = tk.Label(window, text=("Positività: " + str(int((countA/(countA + countB)*100))) + "%" + "\nTotale cellule contate: " + str(countA+countB)), fg="black",font=("Helvetica",16))
    text_risultato.grid(row=12, column=0, pady=10)


text = "Conta cellule per IHC"
text_output = tk.Label(window, text= text, fg="Black", font=("Helvetica",14))
text_output.grid(row=0, column=0, sticky="WE", pady=10)

startBUTTON = tk.Button(text="Avvia nuova conta", command=conta)
startBUTTON.grid(row=1, column=0, sticky="n", pady=10)


# percentualeBUTTON = tk.Button(text="Calcola %", command=risultato)
# percentualeBUTTON.grid(row=2, column=0, sticky="s", pady=10)



if __name__ == "__main__":
    window.mainloop()


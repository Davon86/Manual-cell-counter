from cProfile import label
from ctypes import alignment, resize
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import keyboard
from PIL import Image, ImageTk

# TO DO LIST:
# - V - tasti personalizzabili 
#       - o - in caso di tasti lettera, prevedi anche il blocco maiuscolo.
# - o - salvataggio delle impostazioni su file esterno 
# - o - gestisci il tasto del mouse durante l'acquisizione conta
# - o - riproduci suono quando premuto un tasto sbagliato
#
#  per compilare: pyinstaller contaIHC(v1.2).py --onefile --noconsole

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
    pop.geometry("400x300")
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

def settings():
    global pop_settings

    pop_settings = Toplevel(window)
    pop_settings.title("Impostazioni")
    pop_settings.geometry("500x150")
    pop_set_desc_A = Label(pop_settings, text= "Tasto per cellule positive:         [ " + tastoA + " ]", font=(10))
    pop_set_desc_A.grid(row= 0, column=0, padx=20)
    pop_set_BUTTON_A = tk.Button(pop_settings, text="cambia", command=set_A)
    # pop_set_BUTTON_A = tk.Button(pop_settings, text="cambia", command=premi("A"))
    pop_set_BUTTON_A.grid(row=0, column=1, pady=10, padx=20)
    
    pop_set_desc_B = Label(pop_settings, text= "Tasto per cellule negative:         [ " + tastoB + " ]", font=(10))
    pop_set_desc_B.grid(row= 1, column=0, padx=20)
    pop_set_BUTTON_B = tk.Button(pop_settings, text="cambia", command=set_B)
    # pop_set_BUTTON_B = tk.Button(pop_settings, text="cambia", command=premi("B"))
    pop_set_BUTTON_B.grid(row=1, column=1, pady=10, padx=20)

    pop_set_desc_END = Label(pop_settings, text= "Tasto per interrompere la conta:  [ " + tastoEND + " ]", font=(10))
    pop_set_desc_END.grid(row= 2, column=0, padx=20)
    pop_set_BUTTON_END = tk.Button(pop_settings, text="cambia", command=set_END)
    # pop_set_BUTTON_END = tk.Button(pop_settings, text="cambia", command=premi("END"))
    pop_set_BUTTON_END.grid(row=2, column=1, pady=10, padx=20)

    # pop_set_okBUTTON = tk.Button(pop_settings, text="salva impostazioni")
    # pop_set_okBUTTON.grid(row=3, column=0, sticky="EW", pady=10, padx=10)
    pop_settings.update()

def set_A():
    global tastoA
    keyboardTEMP= ""

    premiTASTO = Toplevel(pop_settings)
    premiTASTO.title("Premi un tasto")
    premiTASTO.geometry("200x45")
    premiTASTO_desc = Label(premiTASTO, text= ">>   Premi un tasto   <<", font=(10))
    premiTASTO_desc.grid(row= 0, sticky="WE", column=0, padx=20, pady=10)
    premiTASTO.update()

    keyboardTEMP = keyboard.read_event(suppress=False)
    tastoA = keyboardTEMP.name

    pop_settings.destroy()
    premiTASTO.destroy()
    settings()
    
def set_B():
    global tastoB
    keyboardTEMP= ""

    premiTASTO = Toplevel(pop_settings)
    premiTASTO.title("Premi un tasto")
    premiTASTO.geometry("200x45")
    premiTASTO_desc = Label(premiTASTO, text= ">>   Premi un tasto   <<", font=(10))
    premiTASTO_desc.grid(row= 0,sticky="WE", column=0, padx=20, pady=10)
    premiTASTO.update()

    keyboardTEMP = keyboard.read_event(suppress=False)
    tastoB = keyboardTEMP.name

    pop_settings.destroy()
    premiTASTO.destroy()
    settings()

def set_END():
    global tastoEND
    keyboardTEMP= ""

    premiTASTO = Toplevel(pop_settings)
    premiTASTO.title("Premi un tasto")
    premiTASTO.geometry("200x45")
    premiTASTO_desc = Label(premiTASTO, text= ">>   Premi un tasto   <<", font=(10))
    premiTASTO_desc.grid(row= 0,sticky="WE", column=0, padx=20, pady=10)
    premiTASTO.update()

    keyboardTEMP = keyboard.read_event(suppress=False)
    tastoEND = keyboardTEMP.name

    pop_settings.destroy()
    premiTASTO.destroy()
    settings()

# def msg_errore(temp):
#     messagebox.showinfo("Information", temp)

text = "Conta cellule per IHC"
text_output = tk.Label(window, text= text, fg="Black", font=("Helvetica",14))
text_output.grid(row=0, column=0, sticky="WE", pady=10)

icon = PhotoImage(file='settingsB2.png')

settingsBUTTON = tk.Button(window, image=icon, width=25,height=25, command=settings)
settingsBUTTON.grid(row=0, column=0, sticky="E", pady=10, padx=10)

startBUTTON = tk.Button(window, text="Avvia nuova conta", command=conta)
startBUTTON.grid(row=1, column=0, sticky="n", pady=10)


# percentualeBUTTON = tk.Button(text="Calcola %", command=risultato)
# percentualeBUTTON.grid(row=2, column=0, sticky="s", pady=10)



if __name__ == "__main__":
    window.mainloop()


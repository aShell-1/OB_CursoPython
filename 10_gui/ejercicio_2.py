"""
En este segundo ejercicio,
tendréis que crear una interfaz sencilla
la cual debe de contener una lista de elementos seleccionables,
también debe de tener un label con el texto que queráis.
"""

import tkinter as tk

def itemSelected(pos):
    pos = lbox1.curselection()
    if  pos != None:
        lbl1.config(text=lbox1.get(tk.ANCHOR))

ilist = ['PSG.LGD','TEAM SPIRIT','OG','OUTSIDERS','EVIL GENIUSES','THUNDER AWAKEN']

master = tk.Tk()
master.title('Lista!!!')
master.resizable(0,0)

lbox1 = tk.Listbox(master, selectmode=tk.SINGLE, height=len(ilist), width=15)
lbox1.grid(row=0, column=0, padx=5, pady=5)

for item in ilist:
    lbox1.insert(tk.END, item)

lbox1.bind('<<ListboxSelect>>', itemSelected)

lbl1 = tk.Label(master, text='NADAREMOS!', width=16)
lbl1.grid(row=0, column=1, padx=5, pady=5)

master.mainloop()
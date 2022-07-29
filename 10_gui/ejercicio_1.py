"""
En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción
que se ha seleccionado y que contenga un botón de reinicio para que deje todo como al principio.
Al principio no tiene que haber una opción seleccionada.
"""

import tkinter as tk

def clearSelection():
    pzimg.configure(file='img/no-image.png')
    bvar.set(None)

def selected():
    pzimg.configure(file='img/pizza-'+str(bvar.get())+'.png')

master = tk.Tk()
master.title('Pizza Pizza!')
master.resizable(0,0)

text1 = tk.Label(text='Seleccione su pizza:', font='bold')
text1.grid(row=0, column=0, columnspan=2, pady=10)

bvar = tk.IntVar()

rbtn1 = tk.Radiobutton(master, text='Americana', variable=bvar, value=1, command=selected)
rbtn1.grid(row=1, column=0, sticky='w', padx=10)
rbtn2 = tk.Radiobutton(master, text='Canadiense', variable=bvar, value=2, command=selected)
rbtn2.grid(row=2, column=0, sticky='w', padx=10)
rbtn3 = tk.Radiobutton(master, text='Hawaiana', variable=bvar, value=3, command=selected)
rbtn3.grid(row=3, column=0, sticky='w', padx=10)

pzimg = tk.PhotoImage(file='img/no-image.png')
lbl1 = tk.Label(master, image=pzimg)
lbl1.grid(row=1, column=1, rowspan=3, padx=20)

btn1 = tk.Button(master, text='Limpiar', command=clearSelection)
btn1.grid(row=4, column=0, columnspan=2, pady=10)

master.mainloop()
import tkinter
from tkinter import *


def accion1():
    sel = selected.get()
    label1.config(text=sel)


def accion2(r):
    return 2


def accion3(r):
    return 3


def accion4(r):
    return 4


# Hagamos la interfaz

window = tkinter.Tk()

# creamos los radio buttons


selected = tkinter.StringVar()
r1 = ttk.Radiobutton(window, text="1", value="1", variable=selected, command=accion1)
r1.grid(column=0, row=1, pady=5, padx=5)

r2 = ttk.Radiobutton(window, text="2", value="2", variable=selected)
r2.grid(column=0, row=2, pady=5, padx=5)

r3 = ttk.Radiobutton(window, text="3", value="3", variable=selected)
r3.grid(column=0, row=3, pady=5, padx=5)

r4 = ttk.Radiobutton(window, text="4", value="4", variable=selected)
r4.grid(column=0, row=4, pady=5, padx=5)

label1 = Label(window)
label1.pack()

window.mainloop()

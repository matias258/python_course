from tkinter import *
from tkinter import ttk



def sel():
    selected = "Seleccionaste : " + v.get()
    label.config(text=selected)

def restart():
    return v.set("5")

window = Tk()
v = StringVar()
v.set("xd")

r1 = Radiobutton(window, text="1", variable=v, value="1", command=sel)
r1.pack(anchor=W)

r2 = Radiobutton(window, text="2", variable=v, value="2", command=sel)
r2.pack(anchor=W)

r3 = Radiobutton(window, text="3", variable=v, value="3", command=sel)
r3.pack(anchor=W)

none_Rb = Radiobutton(window, text="None", variable=v, value="5")
none_Rb.pack(anchor=W)

label = Label(window)
label.pack()

#Creamos el boton

boton = ttk.Button(window, text ="Reinicio", command= restart)
boton.pack()

#No logre resetear los valores, pero intente algo similar: Que al tocar "Reset" vuelva al RadioButton "None"

window.mainloop()

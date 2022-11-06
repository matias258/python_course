#!/usr/bin/python
import tkinter

from tkinter import *

top = tkinter.Tk()
top.title("Primos")
frameCanvas = Frame(top)
frameCanvas.pack(side = TOP)

#estructura de la pag

frameInfo=Frame(top)
frameInfo.config
frameInfo.pack()


#Code to add widgets will go here...


def esPrimo(numero):
    
    
    primo = True
    for i in range (2, int(numero)):
        
        if int(numero) % i == 0:
            primo = primo & False
        else:
            primo = primo & True
    if primo:
        tkMessageBox.showinfo("Es primo")
    else:
        tkMessageBox.showinfo("No es primo")

#Entrada

L1 = Label(top, text = "Entrar un numero") 
L1.pack(side = LEFT)                        #Texto a la izquierda

entry_var = StringVar()
entry = Entry(textvariable = entry_var)
entry.pack()




#Entrada a la derecha


#Boton

button = Button(top, text = "Enter", command=esPrimo)
button.pack()

key_slider = Scale(top, from_=1, to=25, orient = HORIZONTAL, length= 300)
key_slider.pack()



#Codigo es primo
print(esPrimo(numero = entry.get()))

top.mainloop()

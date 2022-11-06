import tkinter
from cifrados import *
from tkinter import ttk

def obtener_box0():
    res = box0.get()
    print(res)

def obtener_box1():
    res1 = box1.get()
    print(res1)

def obtener_box2():
    res2 = box2.get()
    print(res2)


def obtener_box3():
    res3 = box3.get()
    print(res3)

def boton1Presionado(submit_button):
    return True


def boton1Presionado2(submit_button2):
    return True

def calcular(x,y):
    if boton1Presionado:
        return cesar(x, y)


window = tkinter.Tk()
window.title("Cifrados Cesar y Vigenere")
#Creamos la grid

window.columnconfigure(0, weight = 5)

frame1 = ttk.Frame(window)
frame1.grid(column=0, row = 0, sticky=tkinter.NW)
#Creamos los labels y boxes para Cesar

label = tkinter.Label(frame1, text="Cesar")
label.grid(column = 0, row = 0, sticky = tkinter.W, padx = 5, pady = 5)


insert_label = ttk.Label(frame1, text ="Inserte la frase: ")
insert_label.grid(column = 0, row = 1, sticky= tkinter.W, padx = 5, pady = 5)

box0 = ttk.Entry(frame1)
box0.grid(column=1, row = 1, sticky= tkinter.E, padx = 5, pady = 5)

labelNumero = ttk.Label(frame1, text ="Inserte el numero: ")
labelNumero.grid(column = 0, row = 2, sticky= tkinter.W, padx = 5, pady = 5)

box1 = ttk.Entry(frame1)
box1.grid(column=1, row = 2, sticky= tkinter.E, padx = 5, pady = 5)

# Creamos el boton de Submit

submit_button= ttk.Button(frame1, text ="Submit", command = lambda:[obtener_box0(), obtener_box1(), boton1Presionado()])
submit_button.grid (column=1, row =3, sticky=tkinter.E, padx=5, pady= 5)



#Creamos un Frame donde vamos a posicionar el Cifrado Vigenere

frame2 = ttk.Frame(window)
frame2.columnconfigure(15, weight = 3)
frame2.rowconfigure(15, weight = 3)
frame2.grid(column=4, row = 0, sticky=tkinter.NE)

#Lo mismo para vigenere pero en Frame


label2 = tkinter.Label(frame2, text="Vigenere")
label2.grid(column = 0, row = 0, sticky = tkinter.NW, padx = 5, pady = 5)


insert_label2 = ttk.Label(frame2, text ="Inserte la frase: ")
insert_label2.grid(column = 0, row = 1, sticky= tkinter.NW, padx = 5, pady = 5)

box2 = ttk.Entry(frame2)
box2.grid(column=1, row = 1, sticky= tkinter.NE, padx = 5, pady = 5)

labelNumero2 = ttk.Label(frame2, text ="Inserte la key: ")
labelNumero2.grid(column = 0, row = 2, sticky= tkinter.NW, padx = 5, pady = 5)

box3 = ttk.Entry(frame2)
box3.grid(column=1, row = 2, sticky= tkinter.NE, padx = 5, pady = 5)

# Creamos el boton de Submit

submit_button2= ttk.Button(frame2, text ="Submit",command = lambda:[obtener_box2(), obtener_box3()])
submit_button2.grid (column=1, row =3, sticky=tkinter.NE, padx=5, pady= 5)





window.mainloop()


calcular(obtener_box0(),obtener_box1())
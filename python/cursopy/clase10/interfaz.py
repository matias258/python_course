import tkinter
from tkinter import ttk



window = tkinter.Tk()



window.columnconfigure(1, weight=3)

#Empecemos creando el label con el texto que quiero

label = tkinter.Label(window, text = "Aca escribo lo que se me antoja.", bg = "black", fg = "green")
label.grid(column =0, row = 0, sticky = tkinter.W)



#Ahora creamos la lista de elementos seleccionables (List box)

lista = ["Juan", "Maria", "Pedro"]
lista_items = tkinter.StringVar(value = lista)
listbox = tkinter.Listbox(window, height = 4, listvariable = lista_items, bg = "green", fg = "black")
listbox.grid(column = 0, row = 1, sticky = tkinter.W)









window.mainloop()

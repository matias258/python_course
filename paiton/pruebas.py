from tkinter import *

###Creamos la pagina###

root=Tk()
root.geometry ("1200x600+100+80")
root.title("Prueba")


frameCanvas = Frame(root)
frameCanvas.pack (side=TOP)

frameInfo= Frame(root)
frameInfo.config
frameInfo.pack()

###Editemosla mejor###

title= Label(frameInfo, text="Esto es una prueba" ,font =("New TImes Roman", 24))

subtitle= Label (frameInfo, text ="Esto iria abajo", font =("New Times Roman", 15))





root.mainloop()

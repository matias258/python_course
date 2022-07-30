# -*- coding: utf-8 -*-
from tkinter import *

def coder():
    print("J´ai appuye sur le bouton coder")
    messageACoder = text_field.get(1.0,END)
    print(messageACoder)
    messageCode = codage(messageACoder, 5)
    print(messageCode)

def codage(texteACoder, decalage):
    ########################3DECLARATION DES VARIABLES###################################
    alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    alphabet_Code=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    alphabet_Double=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    #ALPHABET_DOUBLE=INTERMEDIAIRE POUR PASSER DE ALPHABET A ALPHABET_CODE
    a=0
    Message_Liste=""
    #########################FIN DES VARIABLES########################################
    for k in range(0,26):
        alphabet_Code[k]=alphabet_Double[decalage+k]#DECALAGE DE K


    for i in texteACoder:#MESSAGE CODE SOUS FORME DE CHAINE DE CARACTERES
        for j in range(0,26):
            if i==alphabet[j]:
                Message_Liste+=alphabet_Code[j]
        a=a+1

    return Message_Liste

################CREATION DE LA PAGE#######################################################
root=Tk()
root.geometry("1200x600+100+80")
root.title("Caesar")

frameCanvas = Frame (root)
frameCanvas.pack (side=TOP)


#############################################################################

#######################################SYSTEME DE STRUCTURE####################
frameInfo=Frame (root)
frameInfo.config
frameInfo.pack ()

##########TEXTE DANS LA PAGE##################################################
titre=Label(frameInfo, text="Le code Caesar",font=("New Times Roman",24))
titre.grid(row=1, column=1)

consigne=Label(frameInfo, text="Donne le message a coder",font=("New Times Roman",18))
consigne.grid(row=3, column=1)
##############################################################################

bouton=Button(text="Coder",command=coder)
bouton.pack()

key_slider = Scale(root, from=1, to=25, orient=HORIZONTAL,length=300)
key_slider.pack()

text_label = Label(root, text="Introduisez votre texte")
text_label.pack()

text_field = Text(root)
text_field.pack()



root.mainloop()

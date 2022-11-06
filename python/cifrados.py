


#Cifrados

#Cifrado Cesar


alfabeto=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
abc2=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


def cesar(palabra, numero):
    
    cifrado = []
    for i in range(0, len(palabra) ):
        for j in range (0, len(alfabeto) - 1):          
            if palabra[i] == alfabeto[j]:
                cifrado.append( alfabeto[j + int(numero)])   
                break
        res = "".join(cifrado)   # convierto la lista en string         
    print(res)
    
# Si encuentro la letra en el alfabeto la agrego a "cifrado".


def search (letra, abc):
    for i in range (0, len(abc)):
        if letra == abc[i]:
            return i                                      
# Sirve para obtener el indice en el alfabeto donde esta la letra, ej: si le ingreso la a ->i = 0, d -> i = 3, ...


        
def Vigenere(palabra, key):
    
    nuevo = []
    for i in range (0, len(palabra)):
        Xi = search(palabra[i], abc)
        Yi = search(key[i], abc)
        posicionNueva = int((Xi + Yi) % 27) # en wikipedia decia: (Xi + Yi) mod 27 = nueva letra (donde 27 es len(abc))
        nuevo.append(abc[posicionNueva])
        cadena = "".join(nuevo) 
    print(cadena)

#Obtengo los indices de las letras de la key y la palabra, hago (xi + Yi) mod 27 y obtengo la nueva letra


"""
print("Cesar --> 1")
print("Vigenere --> 2")

ask = input("¿Que cifrado quiere?: ")

if float(ask) == 1:
    palabra = input("Palabra: ")
    numero = input("numero: ")
    cesar (palabra, numero)
    
elif float(ask) == 2:
    palabra = input("Palabra: ")
    a = palabra.replace(" ", "") # saco los espacios
    
    key = input("key: ")
    b = key.replace(" ", "")
    
    Vigenere(a, b)
 """
    










                
        

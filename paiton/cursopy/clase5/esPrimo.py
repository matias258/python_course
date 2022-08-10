def esPrimo (a):
    primo = True

    for i in range (2,abs(int(a))):
        
        
        if abs(int(a)) % i != 0:
             primo = primo & True
        else:
            primo = primo & False
    if (primo == False):
        print("No es primo")
    else:
         print("Es primo")

esPrimo(a = input("Numero:"))

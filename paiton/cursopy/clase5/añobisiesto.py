def bisiesto(año):
    if abs(int(año)) % 4 == 0:
        print("Es año bisiesto")
    else:
        print("No es año bisiesto")

bisiesto(input("Introduzca el año: "))

#Propuse poner el abs porque existen años antes de Cristo,
#Y me sentiria mal al ignorarlos.

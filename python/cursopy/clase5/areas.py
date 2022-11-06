#Area de triangulo

def areaRectangulo(altura, base):
    a = float(altura) * float(base) / 2
    print("El area del rectangulo es:",a)

def areaCirculo (radio):
    b = 3.14 * float(radio)* float(radio)
    print("El area del circulo es:",b)

altura = input("Altura:")
base = input("Base:")
radio = input("Radio:")


areaRectangulo (altura, base)
areaCirculo(radio)

import math

def area(x1,y1,x2,y2,x3,y3):
    ab = int(math.sqrt((int(x2) - int(x1)) ** 2 + (int(y2) - int(y1)) ** 2))
    bc = int(math.sqrt((int(x3) - int(x2)) ** 2 + (int(y3) - int(y2)) ** 2))
    ac = int(math.sqrt((int(x3) - int(x1)) ** 2 + (int(y3) - int(y1)) ** 2))

    area1 = (ab + bc + ac)/2

    return area1
"""
def trianguloCorrecto(x1,y1,x2,y2,x3,y3):
    ab = int(math.sqrt((int(x2)-int(x1))**2 + (int(y2)-int(y1))**2))
    bc = int(math.sqrt((int(x3)-int(x2))**2 + (int(y3)-int(y2))**2))
    ac = int(math.sqrt((int(x3)-int(x1))**2 + (int(y3)-int(y1))**2))


    if int(ab) < int(ac) & int(bc) < int(ac) & int(ab)  + int(bc) > int(ac):
        return True
    if int(ac) < int(ab)  & int(bc) < int(ab)  & int(ac) + int(bc) > int(ab) :
        return True
    if int(ab)  < int(bc) & int(ac) < int(bc) & int(ab)  + int(ac) > int(bc):
        return True
    else:
        return False
"""
def dentro(x1,y1,x2,y2,x3,y3,xp,yp):
    areap1 = area(xp,yp,x2,y2,x3,y3)
    areap2 = area(x1,y1,xp,yp,x3,y3)
    areap3 = area(x1,y2,x2,y2,xp,yp)

    if area(xp,yp,x2,y2,x3,y3) == areap1 + areap2 + areap3:
        return True
    else:
        return False

def puntos(x1,y1,x2,y2,x3,y3,xp,yp):

    if (dentro(x1,y1,x2,y2,x3,y3,xp,yp)):
        print("El punto P esta dentro del triangulo")
    if (dentro(x1,y1,x2,y2,x3,y3,xp,yp)== False):
        print("El punto P no esta dentro del triangulo")
    else:
        print("No se xd")

    return 0


x1 = input("x1: ")
y1 = input("y1: ")

x2 = input("x2: ")
y2 = input("y2: ")

x3 = input("x3: ")
y3 = input("y3: ")

xp = input("xp: ")
yp = input("yp: ")

puntos(x1,y1,x2,y2,x3,y3,xp,yp)








              
        

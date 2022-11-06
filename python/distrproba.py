from math import *
#factorial, exp(), pi(), sqrt()


#Distribuciones de probabilidad

def binomial(n, p, x):
    binom = (factorial(int(n)) / (factorial(int(n)-int(x))*factorial(int(x)))) *(float(p)**int(x))*(1-float(p))**(n-x)
    print(binom)

def Binomialneg ( r, p,x):
    neg = (factorial(x - 1) / (factorial(r - 1) * factorial((x-1)-(r-1)))) * (p **r) * ((1-p)**(x-r)) 
    print(neg)

def Poisson (landa, x):
    pez = (exp(-float(landa)) * float(landa)**int(x))/(factorial(int(x)))
    print(pez)

def Geometrica (p, x):
    geo = p * (1 - p)**x
    print(geo)

def Exp (landa, x):
    expo = 1 -  exp(-(landa * x))
    print(expo)

def HiperGeo (n, N, M, x):
    hiper = ((factorial(M) / (factorial(x) * factorial(M - x))) * (factorial (N - M) / (factorial(n - x) * factorial ((N-M)-(n-x))))) / (factorial (N) / (factorial(n)*factorial(N-n)))
    print(hiper)

print("Estas distribuciones nos daran la P(x <= X)")
print("Binomial   --> 1")
print("Binomial - --> 2")
print("Poisson    --> 3")
print("Geometrica --> 4")
print("Exp        --> 5")
print("")
ask = input("¿Que distribucion quiere calcular?: ")


if float(ask) == 1:
    n = input("N: ")
    p = input("p: ")
    x = input("x: ")
    binomial(int(n),float(p),float(x))

elif float(ask) == 2:
    r = input("r: ")
    p = input("p: ")
    x = input("x: ")
    Binomialneg(int(r),float(p),int(x))

elif float(ask) == 3:
    x = input("x: ")
    landa = input("landa: ")
    Poisson(float(landa), float(x))

elif float(ask) == 4:
    x = input("x: ")
    p = input("p: ")
    Geometrica (float(p), float(x))

elif float(ask) == 5:
    landa = input("landa: ")
    x = input("x: ")
    Exp(float(landa), float(x))

elif float(ask) == 6:
    n = input("n: ")
    N = input("N: ")
    M = input("M: ")
    x = input("x: ")
    HiperGeo(int(n), int(N), int(M), int(x))

    

numero = input("Meter el numero: ")
res = True;
i = 2;

if float(numero) < 0:
    print ("devolver numero positivo")

while i < float(numero):
        
    if float(numero) % i == 0:
        res = res & False;
    else:
        res = res & True;
    i = i+1;
print (res)
    

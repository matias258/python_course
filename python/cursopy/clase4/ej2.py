inicio = input("Inicio: ")
final = input("Final: ")
lista = []

for i in range (int(inicio), int(final)):
    if i % 2 == 1:
        lista.append(i)
    
print(lista)

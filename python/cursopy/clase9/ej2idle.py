lista = [2, 34, 5, 6, 33, 23, 3, 42, 1]  # No supe como crea un input que te pida una lista, asique cree una dentro
print(len(lista))                                    # del codigo :(
print(lista[4])

def impares(x):
    if lista[x] % 2 == 1:
        return False


print(impares(lista[4]))

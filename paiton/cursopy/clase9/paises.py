import equals as equals

paises = input("Inserte los paises separados por comas: ")
list1 = list(sorted((paises.split(","))))


def igualdad (palabra1, palabra2):
    if palabra1.equals(palabra2):
        return True
    else:
        return False


def nohayrepe(list1):
    igual = False
    for i in range(0,len(list1) - 1):
        if list1[i] == list1[i+1]:
            igual = igual or True
        else:
            igual = igual or False
    if igual:
        print("Tiene al menos 2 paises iguales")
    else:
        print(list1)

nohayrepe(list1)



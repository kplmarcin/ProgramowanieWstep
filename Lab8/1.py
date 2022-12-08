# import random
# lista = []
# def find(l2,wartosc):
#
#     for x in range(0,len(l2)):
#         if wartosc == l2:
#             lista.append(x)
#     return lista
#
# l2 = [random.randint(0,10) for x in range(10)]
# print(l2)
# userIn = int(input("Podaj szukaną wartość: "))
# print(find(lista,userIn))
import random
def find(lista, wartosc):
    lista2 = []
    for i in range(len(lista)):
        if lista[i]==wartosc:
            lista2.append(i)
    return lista2
lista = [random.randint(0,20) for x in range(10)]
print(lista)
userIn=int(input("Podaj szukaną wartość: "))
print(find(lista, userIn))

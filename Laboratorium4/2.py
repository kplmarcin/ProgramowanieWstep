zestaw_1 = []
a = int(input("Podaj liczbę"))
import random
zestaw_1 = [random.randint(1,10) for f in range(a)]
print(zestaw_1)

a = int(input("Podaj liczbę"))
zestaw_2 = [random.randint(5,15) for g in range(a)]
print(zestaw_2)

d = int(input("Podaj liczbę do sprawdzenia"))
if d in (zestaw_1 and zestaw_2):
    print("Liczba należy do obydwu zestawów")
elif d in zestaw_2:
    print("Liczba należy do zestawu 2")
elif d in zestaw_1:
    print('Liczba należy do zestawu 1')
else:
    print("Liczba nie mieści się w zestawach")

zestaw_1_2 = zestaw_1 + zestaw_2
print(zestaw_1_2)
zestaw_1_2.sort()
print(zestaw_1_2)

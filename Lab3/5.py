'''n = int(input"Podaj liczbę studentów:")
n = 3
suma = 0
1: punkty = 20
2: punkty = 30
3: punkty = 5
'''

suma = 0
n = int(input("Liczba studentów:"))
while True:
    x = int(input("Punkty:"))
    suma += x
    print(suma)
print(suma//n)

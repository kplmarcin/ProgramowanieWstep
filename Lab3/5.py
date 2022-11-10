'''n = int(input"Podaj liczbę studentów:")
n = 3
suma = 0
1: punkty = 20
2: punkty = 30
3: punkty = 5
'''

suma = 0
n = int(input("Liczba studentów:"))
x = 1 #liczba od której zaczniemy liczyć
suma = 0 #suma punktów

while (x<=n):
    print("Proszę podać liczbę punktów:", x, end=' ')
    b = int(input())
    x=x+1
    suma=suma+b
z = suma/x
print("Średnia liczba punktów:" , z)



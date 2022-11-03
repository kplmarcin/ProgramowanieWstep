n = int(input("Podaj liczbę studentów: "))
x = 1
s = 0
while True
    p = int(input(f"Podaj liczbę punktów studenta {x}: "))
    if p > 100 or p < 0:
        continue
    x = x+1
    s = s+p
    if(n+1==x):
        break
print("Średnia punktów wynosi:", round(s/n,2))
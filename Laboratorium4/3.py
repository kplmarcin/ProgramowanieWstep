Z = []
a = int(input("Podaj liczbę zwierząt:"))
for b in range(a):
    x = input("Podaj nazwę zwierzęcia:")
    Z.append(x)
print(Z)
Z.sort()
print(Z)
print(Z[0],Z[-3:],len(Z) )


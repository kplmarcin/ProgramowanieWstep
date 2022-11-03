x = int(input("Podaj liczbę kolumn i gwiazdek: "))
for i in range(x):
    for j in range(x):
        print("*", end=" ")
    print("")
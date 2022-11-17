# Zadanie 5. Utwórz listę punkty będącą listą punktów zdobytych z pewnego egzaminu przez grupę 15 studentów.
# Punkty niech będą liczbami rzeczywistymi z przedziału [0; 50]. Następnie
#  Wyświetl informację o największej i najmniejszej ilości zdobytych punktów
# Wyświetl indeks pierwszego wystąpienia punktów podanych przez użytkownika. Jeżeli taka liczba
# punktów nie występuje na liście, wyświetl odpowiedni komunikat
# Oblicz średnią punktów liczbę punktów z egzaminu
#  Oblicz, ile osób zdobyło punkty powyżej, a ile poniżej średniej
#  Wyświetl punkty poniżej średniej
#  Wyświetl punkty powyżej średniej
'''B n = 15
import random
punkty =[]
for x in range(15):
    a = random.uniform(0,50)
    a = round(a,2)
    punkty.append(a)
print(punkty)
print("Wartośc maksymalna: ", max(punkty))
print("Wartośc minimalna: ", min(punkty))
p = float(input("Podaj liczbę punktów: "))
if p in punkty:
    u = punkty.index(p)
    print(u)
else:
    print("Wartośc nie występuje w liście: ")

s = sum(punkty)
print("Średnia: ", round(s/n,2))

punkty_2 = []
for i in range(n):
    if punkty[i] > s:
        punkty_2.append(punkty(i))
print(punkty_2)

for p in punkty:
    if p > sr:
        punkty_2.append(p) KONIEC'''


import random
punkty = []
liczba_stud = 15
for i in range(liczba_stud):
    # punkty = random.random() * 100 % 50
    p = random.uniform(0, 50)
    punkty.append(round(p, 2))
print()
print(punkty)
print(f'min = {min(punkty)}')
print(f'max = {max(punkty)}')
p = float(input('Podaj liczbę punktów: '))
if p in punkty:
    print(punkty.index(p))
else:
    print(f'liczba {p} punktów nie występuje na liście')
print()
y = sum(punkty)
sr = round(y/liczba_stud, 2)
print("Średnia: ", sr)
punkty_w = []
punkty_n = []
for i in range(liczba_stud):
    if punkty[i] > sr:
        punkty_w.append(punkty[i])
punkty_n = [punkty for l in punkty if l < sr]
print("Punkty powyżej średniej: ", punkty_w , len(punkty_w), "Punkty poniżej średniej: ", punkty_n, len(punkty_n))
# Zadanie 5. Utwórz listę punkty będącą listą punktów zdobytych z pewnego egzaminu przez grupę 15 studentów.
# Punkty niech będą liczbami rzeczywistymi z przedziału [0; 50]. Następnie
#  Wyświetl informację o największej i najmniejszej ilości zdobytych punktów
# Wyświetl indeks pierwszego wystąpienia punktów podanych przez użytkownika. Jeżeli taka liczba
# punktów nie występuje na liście, wyświetl odpowiedni komunikat
# Oblicz średnią punktów liczbę punktów z egzaminu
#  Oblicz, ile osób zdobyło punkty powyżej, a ile poniżej średniej
#  Wyświetl punkty poniżej średniej
#  Wyświetl punkty powyżej średniej
n = 15
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
'''od Grażyna Szostek do każdy:    6:47 PM
for p in punkty:
    if p > sr:
        punkty_2.append(p)'''

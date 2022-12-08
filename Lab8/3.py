# import random
# def potęga(l,p):
#     for x in range(len(l)):
#         wyniki = l[x] ** p[x]
#         wynik.append(wyniki)
#         x=+1
#     return(wyniki)
#
#
#
# liczby = [random.randint(0,10) for x in range(50000)]
# potegi =[random.randint(0,5) for x in range(500000)]
# wynik = []
# rezultat = potęga(liczby, potegi)
# print(rezultat)
#
def potega(w,p):
    wyniki = []
    if len(w) != len(p):
        print('listy nie sa tej samej dlugosci')
        return wyniki
    for x in range(len(w)):
         wynik = w[x] ** p[x]
         wyniki.append(wynik)
    return wyniki
wartosci=[2,3,4,5]
potegi=[2,3,4,5]
rezultat=potega(wartosci,potegi)
print(rezultat)
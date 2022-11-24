def z3(*krotka):
    list = []
    for x in krotka:
        print(x)
        list.append(x)

#z3("siema","elo",21.37,4,5,6,"kms")

#z3()

#z3("siemano", [1, 2, 3])

def maximum2(a1,*args):
    pom = a1
    for x in args:
        if pom < x:
            pom = x
    return pom
maks = maximum2(1,2,3,10,30,4,5)
print(maks)

maks = maximum2(2)
print(maks)


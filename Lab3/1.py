x = int(input("Podaj pierwszą liczbę"))
y = int(input("Podaj drugą liczbę"))

if(x>y):
    x, y = y, x
while(x<+y):
    print(x, end = ",")
    x = x + 1



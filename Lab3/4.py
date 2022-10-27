x = int(input("Podaj pierwszą liczbę"))
y = int(input("Podaj drugą liczbę"))

if(x>y):
    x, y = y, x
while(x<+y):
    if x%2==1:
        x = x + 1
        continue
    print(x, end = ",")
    x = x + 1




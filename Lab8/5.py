#Zad.5
def dodawanie(num1, num2):
    return num1 + num2
def odejmowanie(num1, num2):
    return num1 - num2
def mnozenie(num1, num2):
    return num1 * num2
def dzielenie(num1, num2):
    if num2 == 0:
        print("Nie dziel przez 0!")
        return "ERROR"
    return num1 / num2
slownik={'+': dodawanie, '-': odejmowanie, '*': mnozenie, '/': dzielenie}
num1=int(input("Podaj pierwszą liczbę: "))
num2=int(input("Podaj drugą liczbę: "))
znak=input("Podaj znak działania (+,-,*,/): ")
if slownik.get(znak, "error")=="error":
    print("ERROR: znak z poza zakresu!")
else:
    print(slownik[znak](num1, num2))
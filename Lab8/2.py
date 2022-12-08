def sum_of_values(słownik):
    suma = 0
    for v in słownik.values():
        suma = suma + v
    return suma

dict1 = {'data1':10, 'data2':-4, 'data3':2}

s = sum_of_values(dict1)
print(s)
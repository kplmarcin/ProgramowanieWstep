def z5(**kwargs):
    if 'end' in kwargs:
        temp = kwargs['end']
    else:
        temp = '\n'
    print(kwargs)
    for k in kwargs :
        print(k," = ",kwargs[k], end = temp)
z5(dom=1, ulica="jp2", kod_pocztowy='35-255')
print()
z5(dom=2, ulica="jp2", kod_pocztowy='35-255', end = " ")
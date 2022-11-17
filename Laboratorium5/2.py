'''Wypisz wszystkie pary klucz:wartość występujące w słowniku:
sample_dict = {
 "name": "Kelly",
 "surname": "Jones",
 "age": 25,
 "salary": 8000,
 "city": "New york"}
• Utwórz słownik, wybierając ze słownika sample_dict pary o kluczach zapisanych w liście.
Wskazówki:
− przejdź za pomocą pętli po kluczach zapisanych w liście;
− następnie sprawdź, czy dany klucz występuje w słowniku; jeśli występuje, dodaj go (parę
klucz:wartość) do nowego słownika.
• Usuń ze słownika wartości, których klucze występują w liście.
• Sprawdź, czy wartość „Jones” występuje w słowniku.
• Zmień w słowniku klucz ‘city’ na ‘location’.'''


sample_dict = {
 "name": "Kelly",
 "surname": "Jones",
 "age": 25,
 "salary": 8000,
 "city": "New york"}
for k in sample_dict.keys():
    print(f'{k:<10} = {sample_dict[k]:>8}')
for k, v in sample_dict.items():
    print(f'{k:<10} = {v:>8}')

L = ['name', 'salary']
sample_dict_2 = {}
# for x in L:
#     for z in sample_dict:
#         if x==z:
#             sample_dict_2[x] = sample_dict[x]
#             break
# print(sample_dict_2)
# L = ['name', 'salary']
# for x in L:
#     if x in sample_dict_2.keys:
#         if x==z:
#             sample_dict_2[x] = sample_dict[x]
#             break
# print(sample_dict_2)

sample_dict_2 = {x : sample_dict[x] for x in L if x in sample_dict.keys()}
print(sample_dict_2)

d = sample.dict.copy()
for k in L:
    if k in d.keys():
        d.pop(k)
    print(d)
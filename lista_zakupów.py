#Zadanie 1 Moduł 3
lista_zakupów={'piekarnia':['chleb', 'pączek', 'bułki'],'warzywniak':['marchew', 'seler', 'rukola']}
print('Lista zakupów')
lista_zakupów['piekarnia'].append('rogal')
lista_zakupów['warzywniak'].append('burak')
lista_zakupów['mięsny']=['karkówka','podudzie','schabowy']
print(lista_zakupów)
x=0
for keys, values in lista_zakupów.items():
    print(f'Idę do {keys.capitalize()}, kupuję tu następujące rzeczy: {[i.capitalize() for i in values]}')
    values=len(values)
    x+=values
print(f'W sumie kupuję {[x]} produktów.')


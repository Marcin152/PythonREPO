CountryLeaders = {'PL':'Duda', 'US':'Biden'}

#print(CountryLeaders['US'])

CountryLeaders['DE'] = 'Frank-Steinmeier'
#print(CountryLeaders.keys()) #klucze (PL,US)
#print(CountryLeaders.values()) #wartości (Duda, Biden)
#print(CountryLeaders.items()) #klucz i wartość

#print(CountryLeaders.popitem()) #pokazuje wartosc i potem ją usuwa

#print(CountryLeaders.setdefault('FR','Macron')) #ukazuje wartość i dodaje do słownika

#print(CountryLeaders.get('RU')) #ukazuje wartość jeśli jest i nie dodaje do słownika

NewLeaders = {'RU': 'Putin', 'DE': 'Schulz'}
#print(NewLeaders)
CountryLeaders.update(NewLeaders) #dodaje kolejną listę
#print(CountryLeaders)

#exec

chanels = {'Google':'1480', 'Email':'300', 'Natural Traffic':'440', 'TV Spot':'700'}
print(chanels['Email'])

chanelsUpdate = {'Natural Traffic':'520', 'News':'600'}

chanels.update(chanelsUpdate)
print(chanels)
print(chanels.keys())
print(chanels)

chanels.pop('Email')
print(chanels)

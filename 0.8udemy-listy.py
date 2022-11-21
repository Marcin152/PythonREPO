countries = ['FR','US','DE','RU','PL']
countries[1] = 'GB' #Zamienia dany elemnt listy
countries.append('AU') #Dodaje element do listy
countries.insert(2, "CH") #Dodaje element listy na dokladną pozycje
countries.remove('RU') #Usuwa element Rosja
countries.sort() #Sortuje alfabetycznie
countries.reverse() #Odwraca listę

#print(countries.index('GG')) #sprawdza czy dany element wystepuje i jesli tak to na jakiej pozycji
#print(countries.pop(3)) #Ukazuje dany element listy i potem go usuwa, dobre do wyliczania
#print(countries.count('DE'))
newList = 'FI', "SE"
countries.extend(newList)
countriesCopy = countries
countriesCopy.clear()
#print(countries)
#print(countriesCopy)

#exec
hitsTitles = ['Brothers In Arms','Bohemian Rhapsody','Stairway To Heaven','Riders On The Storm','Wish You Were Here']
hitsTitles.append('Child In Time')
hitsTitles.append('Again')
hitsTitles.insert(3,'Hotel California')
hitsTitles.insert(0,'The sound Of Silence')
print(hitsTitles.index('Hotel California'))
hitsTitles.remove('Hotel California')
hitsTitles[0] = 'Enjoy The Silence'
print(hitsTitles)
hitsToRead = hitsTitles.copy()
hitsToRead.reverse()
print(hitsToRead)
hitsToRead.sort()
print(hitsToRead)
print(hitsToRead.pop(0))
print(hitsToRead.pop(1))

additionalSongs = ['Nothing Compares 2 U', 'Wish You Were Here']
hitsToRead.extend(additionalSongs)
print(hitsToRead)

print(hitsToRead.count('Wish You Were Here'))
print(hitsToRead.count('Riders On The Storm'))

hitsToRead.clear()
print(hitsToRead)

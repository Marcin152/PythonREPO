import os
print(os.chdir())

atext = "To jest tekst."
print (atext.endswith('ekst')) #czy tekst w zmiennej atext kończy się na ekst? Jest to fałsz, bo kończy się kropką
print (atext.endswith('ekst.')) #Jest to prawda
print(atext.islower()) #czy tekst jest małymi literami?
print(atext.upper()) #tekst tylko dużymi literami
print(atext.upper().isupper()) #czy tekst jest dużymi literami? tak ponieważ najpierw upper zmieniło ją na duże
                                #a potem zapytaliśmy czy jest dużymi
print(atext.find('jest')) #wyświtla numer znaku, który mamy zapisany w nawiasie, czyli 3
print(atext.find('jest',3)) #pokazuje od którego znaku chcemy szukać
print(atext.replace("T","4")) #zamienia T na 4
print(atext.replace("T","4").replace("o","1").replace("e","2")) #zamienia T na 4
print(atext.split(" ")) #wypisuje osobny wszystkie wyrazy jako tablica
jakisTamNumer = "1000"
#jakisTamNumer+1
print(jakisTamNumer.isdigit()) #sprawdza czy wyglada jak liczba i można ją przekonwertować
print(jakisTamNumer.isdecimal()) #czy to liczba zmiennoprzecinkowa
print(jakisTamNumer.isalpha()) #czy występują literki i tylko one?
print(jakisTamNumer.isalnum()) #czy są liczby i cyfry - czy jest alfanumerczyny

#exec
quote = "A good programmer is someone who always look both ways before crossing a one-way street"
print(quote.upper())
print(quote.lower())
print(quote.endswith('street'))
print(quote.isupper())
print(quote.upper().isupper())
print(quote.find("one"))
print(quote.replace("one"," 1").replace("both","2"))
print(quote.split(" "))
print(quote.isnumeric())
print(quote.isdigit())
print(quote.isalpha())
print(quote.isalnum())

import string
import time
import sys
print(sys.version)
# line  = "this IS a very STRANGE text"
#
# print(line.capitalize()) #zaczyna od duzej
# print(line.title()) #do kazdego slowa dodaje duza litere
# print(line.upper()) #powieksza wszystkie
# print(line.lower()) #zmniejsza wszystkie
# print(line.swapcase()) #duze na male i odwrotnie
# print(line.casefold()) # tlumaczy inne znaki na zwyczajne odpowiedniki
#
# print(line.count("e"))
# print(line.find("e"))
# print(line.rfind("e"))
# print(line.index("e"))
# print(line.rindex("e"))
# print(line.find("p"))
# print(line.index("p"))
#
# print(line.startswith('this')) #zwraca wartosc ture lub false kiedy zaczyna sie na
# print(line.endswith('THis')) #zwraca wartosc true  lub fals kiedy konczy sie na
# line = """asdkjbashjkdbas
# as
# d
# asd
# as
# da
# sdasdasd
# asdasda
# sd
# """
# #string ascii letters - caly alfabet
# #string ascii digits - wszystkie cyfy
# print(line.count("\n"))
#
# x = string.ascii_letters
# print(x)
# print(string.digits)
# line = "this is the end of this lesson"
# print(line.split(' '))
# list = line.split()
#
# print(" ".join(list))

#LAB

# poem = ''' Orzeł Polaków.
# 1.Runą i w łunach spłoną pożarnych
# Krzyże kościołów, krzyże ofiarne
# I w bezpowrotnym zgubi się szlaku
# W lechickiej ziemi
# 2.O, jasne słońce- wodzu Stalinie!
# Niech sława twoja nigdy nie zginie
# Niechaj jak orły powiedzie z gniazda
# Rosja i z Kremla płonąca gwiazda.
# 3.Na ziemskim globie flagi czerwone
# Będą na wiatrach grały jak dzwony
# Czerwona Armia i wódz jej Stalin
# Odwiecznych wrogów na zawsze obali!
# 4.Zaćmisz się rychło w czarnej godzinie
# Polsko- Twe córy i syny,
# Wiara i każdy krzyż na mogile,
# U stóp am legą w prochu i pyle!
# '''
# lines = poem.split("\n")
#
# for line in range(8):
#     print(lines[line])
#     print(lines[line+8])

# print(time.clock(),time.localtime(time.clock()))
print(time.perf_counter(),time.localtime(time.perf_counter()))



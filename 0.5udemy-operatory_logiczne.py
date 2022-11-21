isWeekend = True

print("Is weekend = ",isWeekend) #określamy zmienne i ich parametry

temperature = 25
print("Temperature = ", temperature)

toDoList = ""
print("toDoList = ",toDoList)

isHappy = isWeekend and temperature >=20 and toDoList == ""  #z ich pomocą możemy przyrównać  wszystkie potrzebne nam
                                                             #atrubuty do wspólnego wyniku, jeśli jeden z parametrów
                                                             #nie będzie spełniał wymogu, zostanie zwrócony wynik false
                                                             #(w tym przypadku temperetura nie jest wystarczająca, dlatego zwraca nam wynik: isHappy = False)
print("Is happy = ", isHappy)

isHappy = not isWeekend and temperature <20 and toDoList != ""  # warunki spełniające isHappy to:
                                                                # obecny dzień to nie weekend, temperatura jest mniejsza niż 20 stopni oraz
                                                                # mamy coś do zrobienia na liście naszych zadań
print("Is happy = ", isHappy)

isHappy = isWeekend and temperature >=20 and toDoList == "" \
          or not isWeekend and temperature <20 and toDoList != ""
print("Is happy = ",isHappy)

isHappy = isWeekend and temperature >=20 and toDoList == "" \
          or not isWeekend and not (temperature >= 20 and toDoList != "")
print("Is happy = ",isHappy)
print("------------------------------")
#exec

isAutomaticMode = False
print("Is automatic mode = ",isAutomaticMode)

is80PercentLight = False
print("Is80PercentLight = ",is80PercentLight)

isDirectLight = False
print("IsDirectLight = ",isDirectLight)

isRainy = False
print("IsRainy = ",isRainy)


lightOn = isAutomaticMode == True and (not is80PercentLight or isDirectLight or isRainy)
print("Light's ON = ",lightOn)
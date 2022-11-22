print('FR')
France = 'FRR' #deklarowanie zmiennych odwrotne
print(France)

pi = 3.14
r = 10
print(pi, r)
print(pi*r**2) #do potegi pisze sie jako **(potega)
#x =  int(input("podaj promien kola: ")) #skrypt na liczenie kola
#print(pi*x*x)

print(1,2,3) # bez odstepow
print(1,2,3, sep='-') # z myślnikiem
print(1,2,3, sep="\n") # w nowej linijce
print(1,2,3, sep="\t") # z tabulatorem
print("To jest dzwonek: \a ") # dzownek windows ale tutaj nie działa
print("\u03A3") # format unicode
print("backslash  \\\\") #pokazuje backslash

#exec
print("TVP1", "TVP2", "TVN", "Polsat", "BBC", "HBO", "MTV",sep=";")
print("TVP1", "TVP2", "TVN", "Polsat", "BBC", "HBO", "MTV",sep=" but better is ")
ProgramName = "BBC"
Item = "News"
Time = "18:00"
print("I like watching ", Item, " at ", Time, " on ", ProgramName,". ", sep="")

five = 5
three = 3
print(five * three)
print(type(five))
print(type(five * three)) #typ zmiennej, która w tym przypadku będzie int
print(five/three)
print(type(five/three)) #polecenie type ukazuje typ zmiennej, która w tym przpadku będzie float


import sys #importuje bibliotekę liczb większych i bardziej dokładnych
sys.maxsize #ukazuje możliwą dokładność
print(sys.maxsize)
veryBigValue = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999 #nawet takie liczby będą liczone bez przybliżenia
print(veryBigValue)
print(type(veryBigValue))
print(veryBigValue+1) #wartość podana w w int czyli jako liczba całkowita
print(veryBigValue+1/2) #mimo że wynik działania to liczba całkowita to typ zmiennej jest zadeklarowany jako flaot(zmiennoprzecinkowa)
#dzieje się tak ponieważ jest to wartość przybliżona
print(type(veryBigValue+1/2))
print(five//three) #dzielenie całkowite w tym przypadku 5:3 = 1
print(five % three) #reszta z dzielenia czyli tzw. dzielenie mudolo(5:3=1 i reszta 2 czyli wynik to 2)
print(float("inf")) #inf, jest skrótem od infinity czyli nieskończonośći
print(float("inf")>99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
 #w tym przypadku zwracana wartość zawsze będzie true, ponieważ nieskończoność jest większa od każdej liczby
print(-float("inf")>9) # nieskończoność w drugą stronę czyli minus

#exec
name = "Marcin"
age = 21
daysInYear = 365
message = "%s is %d old, so is about %d days old"
print(message % (name,age,daysInYear))
name = "Olimpia"
age = 23
message = "{0:s} is {1:d} years old, so is about {2:d} days old"
print(message.format(name,age,daysInYear))
one = 123456789
two = 12345
print(one//two)
print( one % two)
print("123456789 divived by 12345 is ",123456789//12345,"and the rest is ",123456789 % 12345)
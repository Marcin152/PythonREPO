# x_male = 3.1412319263812736
# y_duze = 3.89123123123
#
import math
#
# print(math.ceil(x_male),math.ceil(y_duze)) #Najmniejsza, która jest większa czyli z 3,8 to 4
# print("\n")
#
# print(math.floor(x_male),math.floor(y_duze))#Największa, która jest mniejsza czyli 3 z 3,8 czy 3,1
# print("\n")
#
# print(math.ceil(-x_male),math.ceil(-y_duze))#Najmmiejsza liczba większa od -3,14 czyli -3
# print("\n")
#
# print(math.floor(-x_male),math.floor(-y_duze))#Największa liczba mniejsza od -3,14 czyli -4
# print("\n")
#
# print(pow(2,8),pow(9,0.5))
# print("\n")
#
# print(math.sqrt(16))
# print("\n")
#
# print(math.pi,math.e)
# print("\n")
#
# print(math.sin(math.pi/2),math.cos(math.pi/4))
# print("\n")

#LAB

degree = 45
# 1° = (π * rad)/180
# 1 rad = 180°/π
print(math.radians(45))
y = (degree * math.pi)/180
print(y)

small_r = 22
big_r = 27
family_r = 38
small_p = 11.5
big_p = 15.60
family_p = 22.00

s = math.pi * math.pow(0.22,2)
s2 = math.pi * small_r**2
b = math.pi * math.pow(0.27,2)
f = math.pi * math.pow(0.38,2)
print("The size of pizza in m^2 is:",s)
print("The size of pizza in m^2 is:",b)
print("The size of pizza in m^2 is:",f)
print("The price for the m^2 is: ",small_p/s)
print("The price for the m^2 is: ",big_p/b)
print("The price for the m^2 is: ",family_p/f)
small_pizza_r = 0.22
big_pizza_r = 0.27
family_pizza_r = 0.38

small_pizza_price = 11.50
big_pizza_price = 15.60
family_pizza_price = 22.00

small_area = math.pi * small_pizza_r ** 2
big_area = math.pi * big_pizza_r ** 2
family_area = math.pi * family_pizza_r ** 2




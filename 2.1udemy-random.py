import random

# print("one random number:",random.randint(1,100)) # liczba całkowita od 1 do 100
#
# print("choosing ranndom number from a range", random.choice(range(1,100)))
#
# print("choosing a random number from a range - easier", random.randrange(1,100))
#
# list = ['John', 'Ann', 'Peter','Susan', 'Emily']
# random.shuffle(list)
# print(list)
#
# print("just a random float ",random.random())

#LAB
#1
# i = 1
# while i <= 10:
#     i += 1
#     print("ten random numbers: ",random.randint(1,100))
#2

# x = 0
# number1 = 0
# number2 = -1
# while number2 != number1:
#     number1 = random.randint(1,100)
#     number2 = random.randint(1,100)
#
#     print(number1, number2)
#     x += 1
#     print("try's ",x)


countries = [
    'Uruguay',
    'Russia',
    'Saudi Arabia',
    'Egypt',
    'Spain',
    'Portugal',
    'Iran',
    'Morocco',
    'France',
    'Denmark',
    'Peru',
    'Australia',
    'Croatia',
    'Argentina',
    'Nigeria',
    'Iceland',
    'Brazil',
    'Switzerland',
    'Serbia',
    'Costa Rica',
    'Sweden',
    'Mexico',
    'Korea Republic',
    'Germany',
    'Belgium',
    'England',
    'Tunisia',
    'Panama',
    'Colombia',
    'Japan',
    'Senegal',
    'Poland'ź
    ]
groupNumber = 0
random.shuffle(countries)
#print(len(countries))
x = 1
for x in range (len(countries)):
    if x % 4 == 0:
        groupNumber += 1
        print("Group " ,(groupNumber))
    print(countries[x])
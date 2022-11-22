import random
# myNumbers = []
# twoje_liczby = []
# print("GRA W LOTTO - OBSTAW SWOJE TYPY")
#
# a = input("Podaj liczbe:\n")
# twoje_liczby.append(a)
# int(a)
# print(twoje_liczby)
# b = input("Podaj liczbe:\n")
# twoje_liczby.append(b)
# int(b)
# print(twoje_liczby)
# c = input("Podaj liczbe:\n")
# twoje_liczby.append(c)
# int(c)
# print(twoje_liczby)
# d = input("Podaj liczbe:\n")
# twoje_liczby.append(d)
# int(d)
# print(twoje_liczby)
# e = input("Podaj liczbe:\n")
# twoje_liczby.append(e)
# int(e)
# print(twoje_liczby)
# f = input("Podaj liczbe:\n")
# twoje_liczby.append(f)
# int(f)
# print(twoje_liczby)
# g = input("Podaj liczbe:\n")
# twoje_liczby.append(g)
# int(g)
#
# while len(myNumbers) < 7:
#     newNumber = random.randint(1,49)
#
#     if newNumber in myNumbers:
#         print('Eliminated: ',newNumber)
#         continue
#     myNumbers.append(newNumber)
# print('Twoje liczby to:',twoje_liczby)
# print('Those numbers are:',myNumbers)

#LAB
colors = ['Hearts', 'Bells', 'Acorns', 'Leaves' ]
figures = ['Ace', 'King', 'Queen', 'Jack', '10', '9']
random.shuffle(colors)
random.shuffle(figures)

allCards = []
for c in colors:
    for f in figures:
        allCards.append("%s - %s" % (c, f))
        random.shuffle(allCards)

#print(allCards)
max = len(allCards)
#print(max)
player1 = []
player2 = []
i = 0
while i <= max-2:
    i += 1
    if i % 2 == 0:
        player1.append(allCards[i])
    else:
        player2.append(allCards[i])
print(player1)
print(len(player1))
#
print(player2)
print(len(player2))
#player1 ['Acorns - 10', 'Leaves - 9', 'Bells - Ace', 'Bells - King', 'Hearts - 9', 'Hearts - Jack', 'Leaves - Ace', 'Bells - 10', 'Leaves - Jack', 'Acorns - Ace', 'Leaves - King']
#player2 ['Hearts - 10', 'Hearts - Queen', 'Acorns - 9', 'Acorns - Jack', 'Leaves - Queen', 'Hearts - Ace', 'Hearts - King', 'Bells - Queen', 'Acorns - King', 'Acorns - Queen', 'Leaves - 10', 'Bells - 9']
print("PRZERWA----------------------")
for i in range(max):
    if i % 2 == 0:
        player1.append(allCards[i])
    else:
        player2.append(allCards[i])
print(player1)
print(len(player1))
print(player2)
print(len(player2))
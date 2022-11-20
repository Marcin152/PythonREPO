import random
# numbers = [1]
# print(numbers)
#
# for i in range(20):
#     newNumbers = [1]
#     position = 0
#     while position < len(numbers) -1:
#         newNumbers.append(numbers[position] + numbers[position + 1])
#         position+=1
#
#     newNumbers.append(1)
#
#     numbers = newNumbers.copy()
#
#     print(numbers)

#LAB
# aCard = {"Figure":"King", "Power":12, "Color":'Heart'} SLOWNIK
# print(aCard)
# print(aCard['Figure'])
# print(aCard['Power'])
# print(aCard['Color'])

#Zadanie1

# colors = ['Hearts','Diamonds','Clubs','Spades']
# figures = [
#     {'Figure':'Ace',  'Power':14},
#     {'Figure':'King', 'Power':13},
#     {'Figure':'Queen','Power':12},
#     {'Figure':'Jack', 'Power':11},
#     {'Figure':'10',   'Power':10},
#     {'Figure':'9',    'Power':9}]
# color = ['Red', 'Black']
# allCards = []
# aCard = {}
#
# for c in colors:
#     for f in figures:
#         for x in color:
#             aCard = f.copy()
#             allCards.append(aCard)
#             random.shuffle(allCards)
#
# #print(allCards)
# max = len(allCards)
# player1 = []
# player2 = []
# i = 0
# while i <= max-2:
#     i += 1
#     if i % 2 == 0:
#         player1.append(allCards[i])
#     else:
#         player2.append(allCards[i])
# # print(player1)
# # print(player2)
#
# while len(player1) or 0 and len(player2) > 0:
#     card1 = player1.pop(0)
#     card2 = player2.pop(0)
#     print(card1)
#     print(card2)
#     if card1["Power"] == card2["Power"]:
#         player1.append(card1)
#         player2.append(card2)
#     elif card1.get("Power") > card2.get("Power"):
#         player1.append(card1)
#         player1.append(card2)
#         print()
#     elif card2.get("Power") < card1.get("Power"):
#         player2.append(card2)
#         player2.append(card1)
#         print()
print('------------------------------')
colors = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
figures = [
    {'Figure': 'Ace', 'Power': 14},
    {'Figure': 'King', 'Power': 13},
    {'Figure': 'Queen', 'Power': 12},
    {'Figure': 'Jack', 'Power': 11},
    {'Figure': '10', 'Power': 10},
    {'Figure': '9', 'Power': 9}]

allCards = []
for c in colors:
    for f in figures:
        aCard = f.copy()
        aCard['Color'] = c
        allCards.append(aCard)

import random

random.shuffle(allCards)
print(allCards)

player1 = []
player2 = []

player1 = allCards[:12]
player2 = allCards[12:]

print('-------PLAYER 1--------')
print(player1)

print('-------PLAYER 1--------')
print(player2)

while len(player1) > 0 and len(player2) > 0:
    card1 = player1.pop(0)
    card2 = player2.pop(0)

    if card1["Power"] == card2["Power"]:
        player1.append(card1)
        player2.append(card2)
        # print('=EQUAL \t %d \t %d \t %d \t %d' % (card1["Power"], card2["Power"], len(player1), len(player2)))
        print('=EQUAL \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1) * '*')
    elif card1["Power"] > card2["Power"]:
        player1.append(card1)
        player1.append(card2)
        # print('PLAY-1 \t %d \t %d \t %d \t %d' % (card1["Power"], card2["Power"], len(player1), len(player2)))
        print('PLAY-1 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1) * '*')
    else:
        player2.append(card2)
        player2.append(card1)
        # print('PLAY-2 \t %d \t %d \t %d \t %d' % (card1["Power"], card2["Power"], len(player1), len(player2)))
        print('PLAY-2 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1) * '*')

if len(player1) > 0:
    print('PLAYER 1 WON!!!!')
else:
    ptint('PLAYER 2 WON!!!!')

import random

ints = range(33,127)

password = ''

for i in range(0, 16):
    password += chr(random.choice(ints))

    if i >= 15:
      print(password)

#LAB
import random
# wynik = range(1,7)
# min = 1
# max = 6
#
# for dice in range(1):
#     dice = random.choice((wynik))
#     print(dice)
#
#     if dice == 1:
#         print("o")
#     elif dice == 2:
#         print("oo")
#     elif dice == 3:
#         print("ooo")
#     elif dice == 4:
#         print("oo \n oo")
#     elif dice == 5:
#         print("ooo \n oo")
#     elif dice == 6:
#         print("ooo \n ooo")

#
# dices = []
# min = 1
# max = 6
#
# for x in range(5):
#     dices.append(random.randint(min,max))
#  #   random.shuffle(dices)
#     dices.sort()
# print(dices)

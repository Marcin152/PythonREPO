for liczby in range(1,21): #0 to startowa, 21 to do ilu chcemy dojsc wliczajac to w 0 i 2 to o ile chcemy podnosic kazda petle
    if liczby %2 == 0:
        # print(liczby," jest parzysta")
        print('liczba %2d is %s' % (liczby,'even'))
    else:
        # print(liczby,"nie jest parzysta")
        print('liczba %2d is %s' % (liczby, 'odd'))
print("----------------------------------------")
#LAB
#1
string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'

for j in range(10):
    print(string_A)
print("-----------------------------------------")
#2
for x in range(9):
    if x %2 == 0:
        print(string_A)
    else:
        print(string_B)

print("-----------------------------------------")
#3
for k in range(1,10):
    if k %2 == 0:
        print("x"*k)
    else:
        print("o"*k)

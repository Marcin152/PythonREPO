for x in range (1,6):
    linia = str(x)
    for y in range(1,6):
      # print(x ,"*", y," = ",x*y)
        linia += '\t \t %3d' % (x*y)
    print(linia)
print("----------------------------------------")
#LAB

#1
i = 10
mnoznik = 1

for j in range(1,i+1):
    mnoznik *= j
print(i, mnoznik)
print('-------------------------')

h = 10

for i in range(1,h+1):
    mnoznik = 1

    for j in range(1,i+1):
        mnoznik *= j

    print(i,"!",mnoznik)

print("----------------------")
#2
list_noun = ['dog', 'potato', 'meal', 'icecream', 'car']
list_adj = ['dirty', 'big', 'hot', 'colorful', 'fast']


for noun in list_noun:
    for adj in list_adj:
        print(adj, noun)
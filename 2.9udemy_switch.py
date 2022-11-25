def WeekDayInDeutsch(dayNumber=0):

    days = {
        0: 'der Montag',
        1: 'der Dienstag',
        2: 'der Mittwoch',
        3: 'der Donnerstag',
        4: 'der Freitag',
        5: 'der Samstag',
        6: 'der Sonntag'

    }

    return days.get(dayNumber, 'error')
print(WeekDayInDeutsch())
print(WeekDayInDeutsch(1))
print('-------------------')

#LAB

def GiveGeomSeqElement(a1=2, factor=2,index=64):
    #a1 = first element
    #factor = multiplier
    #index = counted element
    value = a1 * pow(factor,index-1)
    return value
print(GiveGeomSeqElement())
print('--------------')
a1 = 3
factor = 2
index = 5

for i in range(1,index):
    result = GiveGeomSeqElement(a1=a1, factor = factor, index = i)
    print("term: ",i," = ", result)



def forString():

    b = 1
    y = 2
    z = 5

    for i in range(1,z):
        h = i * pow(y,i-1)
        print(h)

forString()

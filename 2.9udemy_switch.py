# def WeekDayInDeutsch(dayNumber=0):
#
#     days = {
#         0: 'der Montag',
#         1: 'der Dienstag',
#         2: 'der Mittwoch',
#         3: 'der Donnerstag',
#         4: 'der Freitag',
#         5: 'der Samstag',
#         6: 'der Sonntag'
#
#     }
#
#     return days.get(dayNumber, 'error')
# print(WeekDayInDeutsch())
# print(WeekDayInDeutsch(1))
# print('-------------------')

#LAB

def GiveGeomSeqElement(a1=2, factor=3,index=4):
    #a1 = first element
    #factor = multiplier
    #index = counted element
    value = a1 * pow(factor,index-1)

    return value
a1 = 2
factor = 3
index = 5
def GiveGeomSeqElement():

    for i in range(1,index):
        result = GiveGeomSeqElement(a1=a1, factor = factor, index = i)
        x = result+result
        print("term: ",i," = ", result,"the",x)
        print(i)



def forString():

    b = 3
    y = 2
    z = 10

    for i in range(1,z):
        h = b * pow(y,i-1)
        print(h)


def GiveFactorForGeomSeq (term, nextterm):
    #wyzancza współczynnik gdy znane są 2 kolejne wyrazy ciągu
    result = nextterm / term
    return result


def GiveSumOfNElemetsGeomSeq(a1 = 2, factor = 3, n = 4):
    #a1 = 1 string
    #factor = multiplier
    # n = number of string
    result = a1*(1-pow(factor,n)) / (1-factor)
    print(result)



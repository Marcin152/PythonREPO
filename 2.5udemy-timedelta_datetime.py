import datetime
import math
import random
# print('Mimimum and maximum', datetime.MINYEAR, datetime.MAXYEAR)
#
# #from datetime import timedelta
#
# d1 = datetime.timedelta(days=1 , hours = 2, minutes=-30)
# print(d1)
#
# d2 = datetime.timedelta(days= 1, hours = -2, minutes=-3)
# print(d2)
#
# print('timedelta sum: ',d1+d2)
# print('------------------------')
#
#
# #from datetime import date
#
# print('Today is', datetime.date.today())
# print('\n')
# print('----------------------------1')
# today = datetime.date.today()
# daysToPay = datetime.timedelta(days = 7)
# print('Today is: ',today)
# print('Bills should be paid within: ',daysToPay,"days")
# print('The bill should be paid till: ', today + daysToPay)
# print('\n')
# print('----------------------------2')
# endOfTheWorld = datetime.date.max
# print('The final end of the wolrld will happen (by Python): ',endOfTheWorld)
# print(endOfTheWorld.weekday())
# print('\n')
# print('----------------------------3')
# bornDate = datetime.date(2000,5,24)
# today = datetime.date.today()
# x = today - bornDate
# x = x / 365
# print(x,"replace days with years")
# print('\n')
# print('----------------------------4')
# print('now()\t',datetime.datetime.now())
# print('today()\t',datetime.datetime.today())
# print('utcnow()\t',datetime.datetime.utcnow())
# print('weekday()\t',datetime.datetime.today().weekday())
# print('\n')
#
# print("%a", datetime.datetime.now().strftime("%a"))
# print("%A", datetime.datetime.now().strftime("%A"))
# print("%w", datetime.datetime.now().strftime("%w"))
# print("%a %A %w", datetime.datetime.now().strftime("%a %A %w"))
# print("%Y-%m-%d_%H_%M_%S_%f",\
#       datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S_%f")
#       )

#from datetime import datetime
#LAB

inputdata = [0,1,2,3,5,8,13,21,34,55,89]
factortable = [0,0.01,0.02, 0.03,0.05,0.08,0.13,0.21,0.34,0.55,0.89]

i = len(inputdata)
f = len(factortable)
# print(i)
# print(f)

if i == f:
    print("DATA PROCESSING - OK")
    for x in range(i):
        minValue = inputdata[x] - factortable[x] * inputdata[x]
        maxValue = inputdata[x] + factortable[x] * inputdata[x]
        print("minValue: ",minValue,"maxValue: ",maxValue)
        mininteger = math.floor(minValue)
        maxinteger = math.ceil(maxValue)
        print(mininteger, inputdata[x], maxinteger)
else:
    print("Input data and factortable need to have equal number of elements!")
print('\n')
print("ODPOWIEDZI TUTAJ \n")
if len(inputdata) == len(factortable):
    i = 0
    while i < len(inputdata):
        minvalue = inputdata[i] - factortable[i] * inputdata[i]
        maxvalue = inputdata[i] + factortable[i] * inputdata[i]
        print('minvalue=', minvalue, 'maxvalue=', maxvalue)

        mininteger = math.floor(minvalue)
        maxinteger = math.ceil(maxvalue)
        print(mininteger, "\t", inputdata[i], "\t", maxinteger)
        i += 1
else:
    print("inputdata and factortable need to have equal number of elements")
print("ZADANIE NUMER 2\n")

for x in range(i):
    minValue = inputdata[x] - random.random() * inputdata[x]
    maxValue = inputdata[x] + random.random() * inputdata[x]
    print("minValue: ",minValue,"maxValue: ",maxValue)
    mininteger = math.floor(minValue)
    maxinteger = math.ceil(maxValue)
    print(mininteger, inputdata[x], maxinteger)

print("ZADANIE NUMERO 3\n")
from datetime import datetime
print(datetime.today())
print(datetime.today().strftime("%Y-%m-%d"))


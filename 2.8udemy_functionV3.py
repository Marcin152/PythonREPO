from datetime import date
from datetime import timedelta

def GiveWorkDay(year=date.today().year,
                month=date.today().month,
                day=date.today().day):
    #prints the nearest working day
    day = date(year, month, day)

    if day.weekday() == 5:
        workingday = day + timedelta(days=2)

    elif day.weekday() == 6:
        workingday = day + timedelta(days=1)

    else:
        workingday = day

    print('working day is: ' ,workingday)
    return

GiveWorkDay()

#LAB

def PrintAnimal(animal=''):
    # this function prints a cat, bear or bat ascii-art
    txt_cat = r'''
|\---/|
| o_o |
 \_^_/'''
    txt_bear = r'''
/  \.-"""-./  \
\    -   -    /
 |   o   o   |
 \  .-'"'-.  /
  '-\__Y__/-'
     `---`'''
    txt_bat = r'''
   /\                 /\
  / \'._   (\_/)   _.'/ \
 /_.''._'--('.')--'_.''._\
 | \_ / `;=/ " \=;` \ _/ |
  \/ `\__|`\___/`|__/`  \/
          \(/|\)/  
     '''

    if animal == 'cat':
        print(txt_cat)
    elif animal == 'bear':
        print(txt_bear)
    elif animal == 'bat':
        print(txt_bat)
    else:
        print("Cannot print '%s'. Correct values for the parameter are: cat, bear, bat" % animal)

    return


PrintAnimal()
# PrintAnimal(animal='bear')
# PrintAnimal(animal='bat')
# PrintAnimal('unicorn')
from datetime import date

def DaysToEndOfYear(year=date.today().year, month=date.today().month, day=date.today().day):


    date_today = date(year, month, day)
    date_end_year = date(year, 12, 31)
    delta = date_end_year - date_today
    print(delta.days)

#
DaysToEndOfYear()
# DaysToEndOfYear(2021, 12, 21)
# DaysToEndOfYear(year=2022, month=12, day=22)
# DaysToEndOfYear(day=23, month=12, year=2023)
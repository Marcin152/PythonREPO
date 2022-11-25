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

    return workingday

nextworkingday = GiveWorkDay(2017,9,2)
print("Next working day after",2017,9,2,'is',nextworkingday)
nextworkingday = GiveWorkDay()
print('Next working day after today is',nextworkingday)

print("Next working day is: ",GiveWorkDay())

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
        return True
    elif animal == 'bear':
        print(txt_bear)
        return True
    elif animal == 'bat':
        print(txt_bat)
        return True
    else:
        print("Cannot print '%s'. Correct values for the parameter are: cat, bear, bat" % animal)
        return False

isTrue = PrintAnimal('cat')
print(isTrue)

#2

def DaysToEndOfYear(year=date.today().year, month=date.today().month, day=date.today().day):


    date_today = date(year, month, day)
    date_end_year = date(year, 12, 31)
    delta = date_end_year - date_today
    return delta.days
#
isFunc = DaysToEndOfYear()
print(isFunc)
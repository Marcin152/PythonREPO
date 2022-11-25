def doAction(action ,parameter):
    print("action: ",action)
    print('parameter:',parameter)
    return

doAction('paint','landscape')
print('-------------------------------')
def doAction2(action ,*parameter):
    print("action: ",action)
    print('parameter:',parameter)
    for element in parameter:
        print('element is: ' ,element)
    return

doAction2('paint','landscape','mountains')
print('--------------------------------')
def doAction3(action ,what,**parameter):
    print("action: ",action)
    print('what" ',what)
    print('parameter:',parameter)
    for element in parameter:
        print(element,'=',parameter[element])
    return

doAction3('sell','car', price = 45, color='grey',type = 'suv')

#LAB
def PrintAnimal(*animals):
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
    for animal in animals:
        if animal == 'cat':
            print(txt_cat)
        elif animal == 'bear':
            print(txt_bear)
        elif animal == 'bat':
            print(txt_bat)
        else:
            print("Cannot print '%s'. Correct values for the parameter are: cat, bear, bat" % animal)


    return
#
# PrintAnimal('cat','bat','doggo','bear')
#2
from datetime import date
def DaysToEndOfYear(*dates):

    for date_today in dates:
        date_end_year = date(date.today().year, 12, 31)
        delta = date_end_year - date_today
        print(date_today,"is",delta.days)

DaysToEndOfYear(date(2022,12,13),date(2011,2,12))
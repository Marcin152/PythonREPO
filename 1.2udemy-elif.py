age = 19
isDrunk = False
isRestrictedArea = False

if age <=18:
    print("too young boi")
else:
    if isDrunk:
        print("are you drunk naoughty boya")
    else:
        if isRestrictedArea:
            print("not here boi")
        else:
            print("it's okay to be wh... I mean to drink")
print("-----")


if age < 18:
    print("yoo young to drink")
elif isDrunk:
    print("you are drunk")
elif isRestrictedArea:
    print("not hereee")
else:
    print("ok")

#exec

owedBooks = False
owedMoney = False
bookCount = 2
onTime = True
isWeekend = True

if isWeekend == True and (owedBooks==False and owedMoney == False and bookCount <=4 and onTime==True):
    print("you can borrow book")
elif isWeekend == True and owedBooks == True:
    print("please give us the rest of ur borrowed books")
elif isWeekend == True and owedMoney == True:
    print("please return your overdue money")
elif isWeekend == True and bookCount >=4:
    print("Too many borrowed books")
elif isWeekend == True and onTime == False:
    print("we cannot borrow you book bcs you don't stick to deadline")
else:
    print("No today, we only work in weekends")

isPizzaOrdered = True
isBigDrinkOrdered = False
isWeekend = False

if isWeekend == False and (isPizzaOrdered == True or isBigDrinkOrdered == True):
    print("You get one free burger coupon")
elif isWeekend == True:
    print("There are no coupons on weekends")
elif isWeekend == False and (isPizzaOrdered == False or isBigDrinkOrdered == False):
    print("Why don't you buy large soda or pizza to get a free burger (only on working days")
elif isWeekend == False and isPizzaOrdered == False:
    print("Buy a large pizza")
elif isWeekend == False and isBigDrinkOrdered == False:
    print("Buy a large soda")

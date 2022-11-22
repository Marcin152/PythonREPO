age = 25

isDrunk = False

if age >=18 and isDrunk != True:
    print("You can buy")
else:
    print("you can't")

#exec

min_likes = 500
min_shares = 100

num_likes = 700
num_shares = 600

if num_likes>=min_likes and num_shares>=min_shares:
    print("The discount is 10%")
else:
    print("No likes and shares-No discount")


isPizzaOrdered = False
isBigDrinkOrdered = True
isWeekend = False

if isWeekend == False and isPizzaOrdered == True or isBigDrinkOrdered == True:
    print("You get one free burger coupon")
else:
    print("Why don't you buy large soda or pizza to get a free burger (only on working days")

diskSize = 170
diskSizeUsed = 133
fileSize = 110

if diskSizeUsed+fileSize<=diskSize:
    print("you can download ur file")
else:
    print("the file is too big")
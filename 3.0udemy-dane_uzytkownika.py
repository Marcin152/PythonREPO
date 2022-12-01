# filename = input('Enter filename: ')
#
# print("The file name is: %s" % filename)
#
#
# while True:
#
#     filesizeStr = input("Enter the max file size (MB): ")
#
#     if filesizeStr.isdecimal():
#         filesizeInt = int(filesizeStr)
#         break
#
#
# print("The max size is %d " % (filesizeInt))
#
# print("Size in KB is %s" % (filesizeInt * 1024))

#LAB

import math


def check_int(s):
    if s[0] in ('-','+'):
        return s[1:].isdigit()
    return s.isdigit()

while True:
    a = input("Press a: ")
    b = input("Press b: ")
    c = input("Press c: ")

    if a.isdecimal() & b.isdecimal() & c.isdecimal():
        a = int(a)
        b = int(b)
        c = int(c)
        break


if a == 0:
    print("To nie jest równanie kwadratowe")
else:
    delta = pow(b,2) - 4 * a * c

    print(delta)


    if delta < 0:
        print("Delta jest mniejsza niż 0")
        print("Brak rozwiązań")
    elif delta == 0:
        print("Delta wynosi 0")
        pierwiastek = math.sqrt(delta)
        x1 = (-b-pierwiastek) / (2*a)
        print("Twoje x1 wynosi: ",x1)

    elif delta > 0:
        print("Delta jest większa niż 0")
        pierwiastek = math.sqrt(delta)
        x1 = (-b - pierwiastek) / (2 * a)
        print("Twoje x1 wynosi: ", x1)
        x2 = (-b + pierwiastek) / (2 * a)
        print("Twoje x2 wynosi: ", x2)
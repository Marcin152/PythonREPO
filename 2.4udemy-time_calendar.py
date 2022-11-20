import time
import calendar
# print("current time is.. unix epoch", time.time())
# print("\n")
# print("current time is.. tuple", time.localtime(time.time()))
# print("\n")
# print("current time is.. for human", time.asctime(time.localtime(time.time())))
# print("\n")
# print("\n\n\n\n\n\n")
#
# #playing with calendar
#
#
#
# print("------------------------------------")
# print(calendar.month(2017,9,w=5,l=2))
# print("------------------------------------")
# print(calendar.month(2017,9))
# print("------------------------------------")
# print('week day is: ',calendar.weekday(2017,9,29))
# print("------------------------------------")
# calendar.setfirstweekday(6)
# print("------------------------------------")
# print(calendar.month(2017,9))
# print("------------------------------------")
# print('week day is: ',calendar.weekday(2017,9,29))
# print("------------------------------------")
# print('is 2020 a leap year? ',calendar.isleap(2022))
# print("------------------------------------")
# print('Leap days 2000-2017', calendar.leapdays(2000,2017))
# print('Leap days 2000-2020', calendar.leapdays(2000,2020))
# print('Leap days 2000-2021', calendar.leapdays(2000,2021))
# print("------------------------------------")
# print(calendar.calendar(2018))

#LAB
print(time.time())
print("------------------------------------")
print("Our current time is: ", time.localtime(time.time()))
print("------------------------------------")
print(calendar.month(2022,5))
print("------------------------------------")
calendar.setfirstweekday(6)
print(calendar.calendar(2022))
print(calendar.month(2022,5))
print(calendar.isleap(2000))
print(calendar.calendar(2019))

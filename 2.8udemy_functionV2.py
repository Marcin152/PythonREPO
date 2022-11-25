from datetime import date
from datetime import timedelta

def GiveWorkDay(year, month, day):
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


GiveWorkDay(2022,5,2)
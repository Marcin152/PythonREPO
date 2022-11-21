# LAB

from datetime import date


def today():
    date_today = date.today()
    print(date_today)
    current_year = date_today.year
    date_end_year = date(current_year, 12, 31)
    delta = date_end_year-date_today
    print(delta.days)


today()

import calendar
print(calendar.calendar(2020))
calendar.prcal(2020)

from datetime import date
calendar.prcal(date.today().year)

## calendar with starting day of the week as Sunday
calendar.setfirstweekday(calendar.SUNDAY)
calendar.prcal(date.today().year)

## month
print(calendar.month(1982, 1))
calendar.prmonth(1982, 1)

## weekday
print(calendar.weekday(1982, 1, 13))

## weekheader
print(calendar.weekheader(5))

## leap year
print(calendar.isleap(2020))
print(calendar.leapdays(2010, 2021))  # Up to but not including 2021.

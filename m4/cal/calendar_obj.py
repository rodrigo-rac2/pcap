import calendar  

c = calendar.Calendar(calendar.SUNDAY)

for weekday in c.iterweekdays():
    print(weekday, end=" ")


##### itermonthdates
### The code displays all days in November 2019. Because the first day of November 2019 was a Friday, the following days are also
# returned to get the complete week: 10/28/2019 (Monday) 10/29/2019 (Tuesday) 10/30/2019 (Wednesday) 10/31/2019 (Thursday).
### The last day of November 2019 was a Saturday, so in order to keep the complete week, one more day is returned 12/01/2019 (Sunday).
c = calendar.Calendar()

for date in c.itermonthdates(2019, 11):
    print(date, end=" ")

print("\n")

#### itermonthdays
# You’ll have certainly noticed the large number of 0s returned as a result of the example code. These are days outside the 
# specified month range that are added to keep the complete week.
c = calendar.Calendar()

for iter in c.itermonthdays(2019, 11):
    print(iter, end=" ")
print("\n")

for iter in c.itermonthdays2(2019, 11):
    print(iter, end=" ")
print("\n")

for iter in c.itermonthdays3(2019, 11):
    print(iter, end=" ")
print("\n")

for iter in c.itermonthdays4(2019, 11):
    print(iter, end=" ")
print("\n")

c = calendar.Calendar()

for data in c.monthdays2calendar(2020, 12):
    print(data)

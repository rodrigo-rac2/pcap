from datetime import date

today = date.today()

print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)

### 
import time

timestamp = time.time()
print("Timestamp:", timestamp)

d = date.fromtimestamp(timestamp)
print("Date:", d)

### 
d = date.fromisoformat('2019-11-04')
print(d)

###
d = date(1991, 2, 5)
print(d)

d = d.replace(year=1992, month=1)
print(d)

###
d = date(2019, 11, 4)
print(d.weekday())
print(d.isoweekday())

d = date(1982, 1, 13)
print(d.weekday())
print(d.isoweekday())

###
from datetime import time

t = time(14, 53, 20, 1)

print("Time:", t)
print("Hour:", t.hour)
print("Minute:", t.minute)
print("Second:", t.second)
print("Microsecond:", t.microsecond)

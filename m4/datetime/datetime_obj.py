from datetime import datetime
from datetime import time

dt = datetime(1982, 1, 13, 16, 0)

print("Datetime:", dt)
print("Date:", dt.date())
print("Time:", dt.time())

print(dt.strftime('%d/%m/%Y'))

print("today:", datetime.today())
print("now:", datetime.now())
print("utcnow:", datetime.utcnow())

dt = datetime(2020, 10, 4, 14, 55)
print("Timestamp:", dt.timestamp())

t = time(14, 53)
print(t.strftime("%H:%M:%S"))

dt = datetime(2020, 11, 4, 14, 53)
print(dt.strftime("%y/%B/%d %H:%M:%S"))

##

import time 

timestamp = 1572879180
st = time.gmtime(timestamp)

print(time.strftime("%Y/%m/%d %H:%M:%S", st))
print(time.strftime("%Y/%m/%d %H:%M:%S"))

##
print(datetime.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))

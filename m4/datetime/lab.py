from datetime import datetime

def get_am_pm(dt):
    hour = dt.hour
    if hour < 12:
        return "AM"
    else:
        return "PM"

dt = datetime.strptime("2020/11/04 14:53:00", "%Y/%m/%d %H:%M:%S")
print(dt.strftime("%Y/%m/%d %H:%M:%S"))
print(dt.strftime(f"%y/%B/%d %H:%M:%S {get_am_pm(dt)}"))
print(dt.strftime(f"%a, %Y %b %d"))
print(dt.strftime(f"%A, %Y %B %d"))
print(f"Weekday: {dt.isoweekday()}")
print(f"Day of the year: {dt.timetuple().tm_yday}")
print(f"Week number of the year: {dt.isocalendar()[1]}")

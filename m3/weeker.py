class WeekDayError(Exception):
    pass
	

class Weeker:
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    def __init__(self, day):
        if day not in self.days:
            raise WeekDayError
        self.day = day

    def __str__(self):
        return self.day

    def add_days(self, n):
        day_index = Weeker.days.index(self.day)
        new_index = day_index + n
        c = 0
        while new_index > 6:
            c += 1
            new_index -= 6
        self.day = Weeker.days[new_index - c]

    def subtract_days(self, n):
        day_index = Weeker.days.index(self.day)
        new_index = day_index - n
        c = 0
        while new_index < 0:
            c += 1
            new_index += 6
        self.day = Weeker.days[new_index + c]
        


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")

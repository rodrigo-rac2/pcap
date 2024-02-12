def format_hour(t):
    hours, minutes, seconds = "", "", ""
    if t.hour < 10:
        hours = f"0{t.hour}"
    else:
        hours = f"{t.hour}"
    if t.minute < 10:
        minutes = f"0{t.minute}"
    else:
        minutes = f"{t.minute}"
    if t.second < 10:
        seconds = f"0{t.second}"
    else:
        seconds = f"{t.second}"
    
    return f'{hours}:{minutes}:{seconds}'
    

class Timer:
    def __init__(self, hour = 0, minute = 0, second = 0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return format_hour(self)

    def next_second(self):
        if self.second == 59:
            self.second = 0
            if self.minute == 59:
                self.minute = 0
                if self.hour == 23:
                    self.hour = 0
                else:
                    self.hour += 1
            else:
                self.minute += 1
        else:
            self.second += 1
        

    def prev_second(self):
        if self.second == 0:
            self.second = 59
            if self.minute == 0:
                self.minute = 59
                if self.hour == 0:
                    self.hour = 23
                else:
                    self.hour -= 1
            else:
                self.minute -= 1
        else:
            self.second -= 1
        

timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)

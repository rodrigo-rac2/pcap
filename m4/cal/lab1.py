import calendar

class MyCalendar(calendar.Calendar):
    def __init__(self):
        super().__init__()
        self.cal = calendar.Calendar()
    
    def count_weekday_in_year(self, year, weekday):
        weekdays = 0
        for month in range(12):
            month_tuple = self.cal.monthdays2calendar(year, month + 1)
            for week in month_tuple:
                for date, wday in week:
                    if wday == weekday and date != 0: weekdays += 1
        return weekdays

if __name__ == "__main__":
    cal_obj = MyCalendar()
    print(cal_obj.count_weekday_in_year(2019, 0))
    print(cal_obj.count_weekday_in_year(2000, 6))
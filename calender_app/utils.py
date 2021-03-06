from calendar import HTMLCalendar
from .models import Event
from dateutil import parser
import datetime
class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    # formats a day as a td
    # filter events by day
    def formatday(self, day, events):
        if len(str(day))==1:
            str_day = "0"+str(day)
        else:
            str_day = str(day)
        events_per_day = events.filter(day=str_day)
        d = ''
        for event in events_per_day:
            d += f'<div class="event mb-1 p-1"> {event.title} </div>'
        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        return '<td></td>'

    # formats a week as a tr
    def formatweek(self, theweek, events):
        week = ''
        for d, weekday in theweek:
            # print(d, weekday)
            week += self.formatday(d, events)
        return f'<tr> {week} </tr>'

    # # formats a month as a table
    # # filter events by year and month
    def formatmonth(self, withyear=True):
        if len(str(self.month))==1:
            month = "0"+str(self.month)
        else:
            month = str(self.month)
        events = Event.objects.filter(year=str(self.year),month=month)
        cal = '<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, events)}\n'
        return cal

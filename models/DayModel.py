

from datetime import datetime, date


class Day(object):

    def __init__(self,
                 day_count: int,
                 is_monday: bool = False,
                 is_tuesday: bool = False,
                 is_wednesday: bool = False,
                 is_thursday: bool = False,
                 is_friday: bool = False,
                 is_saturday: bool = False,
                 is_sunday: bool = False,
                 ):
        self.day_count = day_count
        self.is_monday = is_monday
        self.is_tuesday = is_tuesday
        self.is_wednesday = is_wednesday
        self.is_thursday = is_thursday
        self.is_friday = is_friday
        self.is_saturday = is_saturday
        self.is_sunday = is_sunday

    @staticmethod
    def get_today(some_date: str):
        d0 = datetime.strptime(some_date, '%Y.%m.%d').date()
        d1 = date.today()
        delta = d1 - d0
        print()
        print(delta.days)
        print()
        return Day(delta.days + 1)

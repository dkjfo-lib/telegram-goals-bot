
from models.DayModel import Day


class Schedule(object):

    def __init__(self,
                 first_day: int,
                 is_on_monday: bool,
                 is_on_tuesday: bool,
                 is_on_wednesday: bool,
                 is_on_thursday: bool,
                 is_on_friday: bool,
                 is_on_saturday: bool,
                 is_on_sunday: bool,
                 is_every_day: bool,
                 is_every_two_days: bool,
                 is_every_three_days: bool,
                 is_every_four_days: bool,
                 ):
        self.first_day = first_day
        self.is_on_monday = is_on_monday
        self.is_on_tuesday = is_on_tuesday
        self.is_on_wednesday = is_on_wednesday
        self.is_on_thursday = is_on_thursday
        self.is_on_friday = is_on_friday
        self.is_on_saturday = is_on_saturday
        self.is_on_sunday = is_on_sunday
        self.is_every_day = is_every_day
        self.is_every_two_days = is_every_two_days
        self.is_every_three_days = is_every_three_days
        self.is_every_four_days = is_every_four_days

    def is_on_this_day(self, day: Day) -> bool:
        if self.is_every_day:
            return True
        if self.is_on_monday and day.is_monday:
            return True
        if self.is_on_tuesday and day.is_tuesday:
            return True
        if self.is_on_wednesday and day.is_wednesday:
            return True
        if self.is_on_thursday and day.is_thursday:
            return True
        if self.is_on_friday and day.is_friday:
            return True
        if self.is_on_saturday and day.is_saturday:
            return True
        if self.is_on_sunday and day.is_sunday:
            return True
        if self.is_every_two_days:
            if day.day_count - self.first_day % 2 == 0:
                return True
        if self.is_every_three_days:
            if day.day_count - self.first_day % 3 == 0:
                return True
        if self.is_every_four_days:
            if day.day_count - self.first_day % 4 == 0:
                return True
        return False

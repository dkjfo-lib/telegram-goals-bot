
class Day(object):

    def __init__(self, 
            day_count : int,
            is_monday :bool,
            is_tuesday :bool,
            is_wednesday :bool,
            is_thursday :bool,
            is_friday :bool,
            is_saturday :bool,
            is_sunday :bool,
            ):
        self.day_count = day_count
        self.is_monday = is_monday
        self.is_tuesday = is_tuesday
        self.is_wednesday = is_wednesday
        self.is_thursday = is_thursday
        self.is_friday = is_friday
        self.is_saturday = is_saturday
        self.is_sunday = is_sunday
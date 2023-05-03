from uuid import UUID
from models.ScheduleModel import Schedule

class Task(object):

    def __init__(self, name: str, id :UUID, schedule :Schedule, is_active :bool):
        self.name = name
        self.id = id
        self.schedule = schedule
        self.is_active = is_active

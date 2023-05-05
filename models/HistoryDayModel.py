import datetime as Datetime
from typing import List
from models.HistoryTaskModel import HistoryTask


class HistoryDay(object):

    def __init__(self,
                 tasks: List[HistoryTask],
                 datetime: Datetime,
                 day_count: int,
                 ):
        self.tasks = tasks,
        self.date = datetime,
        self.day_count = day_count,

    def serialize_self(self):
        return {
            'date': self.date,
            'tasks': list(map(lambda x: x.serialize_self(), self.tasks)),
            'day_count': self.day_count,
        }

    @staticmethod
    def deserialize_self(schema):
        return HistoryDay(
            tasks=list(map(lambda x: HistoryTask.deserialize_self(x), schema['tasks'])),
            date=schema['date'],
            day_count=schema['day_count']
        )

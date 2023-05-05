from typing import List
from models.HistoryDayModel import HistoryDay
from models.TaskModel import Task


class User(object):

    def __init__(self, tg_id: int, tasks: List[Task], history: List[HistoryDay], birth_day: str, time_zone :int):
        self.tg_id = tg_id
        self.tasks = tasks
        self.history = history
        self.birth_day = birth_day
        self.time_zone = time_zone

    def serialize_self(self):
        return {
            'tg_id': self.tg_id,
            'tasks': list(map(lambda x: x.serialize_self(), self.tasks)),
            'history': list(map(lambda x: x.serialize_self(), self.history)),
            'birth_day': self.birth_day,
            'time_zone': self.time_zone,
        }

    @ staticmethod
    def deserialize_self(schema):
        print()
        print()
        print(schema)
        print(schema['tg_id'])
        print()
        return User(
            tg_id=schema['tg_id'],
            tasks=list(
                map(lambda x: Task.deserialize_self(x), schema['tasks'])),
            history=list(
                map(lambda x: HistoryDay.deserialize_self(x), schema['history'])),
            birth_day=schema['birth_day'],
            time_zone=schema['time_zone'],
        )


from models.TaskModel import Task


class HistoryTask(object):

    def __init__(self,
                 task: Task,
                 completed: bool
                 ):
        self.name = task.name,
        self.id = task.id,
        self.completed = completed

    def serialize_self(self):
        return {
            'name': self.name,
            'id': self.id,
            'completed': self.completed,
        }

    @staticmethod
    def deserialize_self(schema):
        return Task(
            name=schema['name'],
            id=schema['id'],
            completed=schema['completed'],
        )

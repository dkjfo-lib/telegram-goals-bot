from uuid import UUID
from models.ScheduleModel import Schedule


class Task(object):

    def __init__(self, name: str, id: UUID, schedule: Schedule, is_active: bool):
        self.name = name
        self.id = id
        self.schedule = schedule
        self.is_active = is_active

    def serialize_self(self):
        return {
            "name": self.name,
            "id": str(self.id),
            "schedule": self.schedule.serialize_self(),
            "is_active": self.is_active
        }

    @staticmethod
    def deserialize_self(schema):
        return Task(
            name=schema["name"],
            id=UUID(schema["id"]),
            schedule=Schedule.deserialize_self(schema["schedule"]),
            is_active=schema["is_active"]
        )

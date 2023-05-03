from asyncio import Task
from typing import List


class User(object):

    def __init__(self, tg_id :int, tasks :List[Task]):
        self.tg_id = tg_id
        self.tasks = tasks

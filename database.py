import logging
import os
from typing import List
from pymongo import MongoClient
from models.HistoryDayModel import HistoryDay
from models.HistoryTaskModel import HistoryTask
from models.TaskModel import Task
from models.UserModel import User

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def get_collection():
    MONGODB_CONNECTION_STRING = os.getenv('MONGODB_CONNECTION_STRING')
    client = MongoClient(MONGODB_CONNECTION_STRING)
    db = client['Goals_Users']
    collection = db["Goals_Users"]
    return collection


def is_user_exists(tg_id: int):
    collection = get_collection()
    return collection.count_documents({'tg_id': tg_id}, limit=1) != 0


def save_user(user: User):
    collection = get_collection()
    user_scheme = user.serialize_self()
    if is_user_exists(user.tg_id):
        query = {"tg_id": user.tg_id}
        set_user_scheme = {"$set": user_scheme}
        collection.update_one(query, set_user_scheme)
        logger.info(f'user "{user.tg_id}" updated')
    else:
        collection.insert_one(user_scheme)
        logger.info(f'user "{user.tg_id}" created')


def load_user(tg_id: int) -> User:
    collection = get_collection()
    user_info = collection.find_one({'tg_id': tg_id})
    logger.info(f'user "{tg_id}" loaded')
    user = User.deserialize_self(user_info)
    return user


def erase_user(tg_id: int):
    collection = get_collection()
    collection.delete_one({'tg_id': tg_id})
    logger.info(f'user "{tg_id}" deleted')

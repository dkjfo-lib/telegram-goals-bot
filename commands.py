import logging
from uuid import uuid4
from telegram import Update
from telegram.ext import ContextTypes
from database import erase_user, is_user_exists, load_user, save_user
from models.DayModel import Day
from models.ScheduleModel import Schedule
from models.TaskModel import Task
from models.UserModel import User


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def is_user_task_exists(user: User, task_name: str):
    target_task = None
    for task in user.tasks:
        if task.name == task_name:
            target_task = task
    return target_task


async def create_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info(f'command: {update.message}')
    user_id = update.effective_user.id

    birth_date = context.args[0]
    time_zone = int(context.args[1])
    user = User(user_id, [], [], birth_date, time_zone)

    if is_user_exists(user_id):
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Your account already exists!")
    else:
        save_user(user)
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Your account was created!")


async def delete_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info(f'command: {update.message}')
    user_id = update.effective_user.id
    if is_user_exists(user_id):
        erase_user(user_id)
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Your account was deleted!")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Your account does not exists!")


async def create_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info(f'command: {update.message}')
    user_id = update.effective_user.id
    args_count = len(context.args)

    task_name = ''
    for i in range(args_count):
        task_name += str(context.args[i]) + ' '
    task_name = task_name.strip()

    if not is_user_exists(user_id):
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Your account was not found!')
        return
    user = load_user(user_id)
    if is_user_task_exists(user, task_name):
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Task "{task_name}" already exists!')
        return

    day = Day.get_today(user.birth_day)
    user.tasks.append(Task(name=task_name, id=uuid4(), schedule=Schedule(first_day=day.day_count,
                                                                         is_every_day=True), is_active=True))
    save_user(user)

    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Task "{task_name}" was created!')


async def disable_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info(f'command: {update.message}')
    user_id = update.effective_user.id
    args_count = len(context.args)

    task_name = ''
    for i in range(args_count):
        task_name += str(context.args[i]) + ' '
    task_name = task_name.strip()

    if not is_user_exists(user_id):
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Your account was not found!')
        return
    user = load_user(user_id)
    if not is_user_task_exists(user, task_name):
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Task "{task_name}" was not found!')
        return

    for task in user.tasks:
        if task.name == task_name:
            task.is_active = False
    save_user(user)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Task "{task_name}" was disabled!')


async def enable_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info(f'command: {update.message}')
    user_id = update.effective_user.id
    args_count = len(context.args)

    task_name = ''
    for i in range(args_count):
        task_name += str(context.args[i]) + ' '
    task_name = task_name.strip()

    if not is_user_exists(user_id):
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Your account was not found!')
        return
    user = load_user(user_id)
    if not is_user_task_exists(user, task_name):
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Task "{task_name}" was not found!')
        return

    for task in user.tasks:
        if task.name == task_name:
            task.is_active = True
    save_user(user)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Task "{task_name}" was enabled!')


async def delete_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info(f'command: {update.message}')
    user_id = update.effective_user.id
    args_count = len(context.args)

    task_name = ''
    for i in range(args_count):
        task_name += str(context.args[i]) + ' '
    task_name = task_name.strip()

    if not is_user_exists(user_id):
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Your account was not found!')
        return
    user = load_user(user_id)
    target_task = is_user_task_exists(user, task_name)
    if not target_task:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Task "{task_name}" was not found!')
        return

    user.tasks.remove(target_task)
    save_user(user)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Task "{task_name}" was deleted!')


async def display_tasks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info(f'command: {update.message}')
    user_id = update.effective_user.id

    if not is_user_exists(user_id):
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Your account was not found!')
        return

    message = 'Your current Tasks:\n'
    user = load_user(user_id)
    for task in user.tasks:
        message += f'    {task.name}\n'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)


async def display_todays_tasks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info(f'command: {update.message}')
    user_id = update.effective_user.id

    if not is_user_exists(user_id):
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Your account was not found!')
        return

    user = load_user(user_id)
    day = Day.get_today(user.birth_day)
    message = f'Today is {day.day_count}th day of your life!\nHere are your goals for today:\n'
    for task in user.tasks:
        message += f'    {task.name}\n'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)

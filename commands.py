import logging
from telegram import Update
from telegram.ext import ContextTypes


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger()
logger.setLevel(logging.INFO)


async def check_if_user_exists(user_id: int) -> bool:
    return True


async def check_if_task_exists(task_name: str) -> bool:
    return True


async def check_task_operation(user_id: int, task_name: str) -> str:
    error_message = ''
    if not await check_if_user_exists(user_id):
        error_message = f'Your account was not found!'
    elif not await check_if_task_exists(task_name):
        error_message = f'Task "{task_name}" was not found!'
    return error_message


async def create_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info(f'command: {update.message}')
    user_id = update.effective_user.id
    if await check_if_user_exists(user_id):
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Your account already exists!")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Your account was created!")


async def create_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info(f'command: {update.message}')
    user_id = update.effective_user.id
    task_name = str(context.args[0])
    error_message = await check_task_operation(user_id, task_name)
    if error_message:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=error_message)
        return
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Task "{task_name}" was created!')


async def disable_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info(f'command: {update.message}')
    user_id = update.effective_user.id
    task_name = str(context.args[0])
    error_message = await check_task_operation(user_id, task_name)
    if error_message:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=error_message)
        return
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Task "{task_name}" was disabled!')


async def enable_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info(f'command: {update.message}')
    user_id = update.effective_user.id
    task_name = str(context.args[0])
    error_message = await check_task_operation(user_id, task_name)
    if error_message:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=error_message)
        return
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Task "{task_name}" was enabled!')


async def delete_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info(f'command: {update.message}')
    user_id = update.effective_user.id
    task_name = str(context.args[0])
    error_message = await check_task_operation(user_id, task_name)
    if error_message:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=error_message)
        return
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Task "{task_name}" was deleted!')

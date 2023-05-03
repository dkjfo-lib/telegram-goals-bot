import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info(f'command: {update.message}')
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def launch_bot():
    TOKEN = os.getenv('BOT_TOKEN')
    LOCAL = bool(int(os.getenv('LOCAL')))
    WEBHOOK = os.getenv('WEBHOOK_URL')
    PORT = int(os.getenv('PORT'))
    IP = os.getenv('IP')
    
    logger.info(f'creating bot with token:"{TOKEN}"...')
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    logger.info(f'bot successfully created.')
    
    if LOCAL:
        logger.info('polling messages...')
        application.run_polling()
    else:
        logger.info(f'setting webhook on "{WEBHOOK}" listening on address "{IP}:{PORT}"...')
        application.run_webhook(
            listen=IP, 
            port=PORT, 
            url_path=TOKEN, 
            webhook_url=WEBHOOK)
        logger.info(f'Webhook deployed!')
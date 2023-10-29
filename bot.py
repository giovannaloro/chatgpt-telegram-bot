import logging 
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters 
import tools
import os 

#telegram functionalities setting
temperature = 0.3

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level = logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hi i am a chatgpt bot, ask anything i will answer!"
    )

async def set_temp(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global temperature 
    temperature = float(context.args[0])
    print(temperature)
    print(context.args) 

async def give_temp(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=temperature)

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    openai_key = os.getenv("OPENAI_API_KEY")
    gpt_answer = tools.ask_gpt(openai_key, update.message.text)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=gpt_answer)

if __name__ == '__main__':
    telegram_key = os.getenv("TELEGRAM_API_KEY")
    application = ApplicationBuilder().token(telegram_key).build()    
    start_handler = CommandHandler('start', start)
    set_temp = CommandHandler('setTemp', set_temp)
    give_temp = CommandHandler('giveTemp', give_temp)
    chat_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), chat)
    application.add_handler(start_handler)
    application.add_handler(set_temp)
    application.add_handler(give_temp)
    application.add_handler(chat_handler)    

#run bot 
    application.run_polling()
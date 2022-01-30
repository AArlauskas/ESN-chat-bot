from telegram import Bot, ParseMode
import env
from event import Event
import repository

bot = Bot(env.TELEGRAM_TOKEN)

def sendNewEventMessage(event: Event):
    text = "\nNew ESN event is here!\n" + event.toString()
    tokens = repository.getAllTokens()
    for token in tokens:
        bot.sendMessage(chat_id=token,
                    text=text,
                    parse_mode=ParseMode.HTML)
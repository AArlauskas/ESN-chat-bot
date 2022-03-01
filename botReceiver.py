from telegram import KeyboardButton, ReplyKeyboardMarkup, Update
from telegram.ext import Updater, Filters, CommandHandler, MessageHandler

import repository
import messageTypes
import env
import eventsService
import tokensService
from event import Event

updater = Updater(token=env.TELEGRAM_TOKEN, use_context=True)
dispatcher = updater.dispatcher

def messageHandler(update: Update, context):
    messageType = update.message.text
    
    if messageType == messageTypes.INSTALL:
        install(update, context)
    elif messageType == messageTypes.REMOVE:
        remove(update, context)
    elif messageType == messageTypes.NOW:
        now(update, context)
        
def start(update, context):
    message = "Commands:\n install - adds telegram account to receive notifications.\n remove - removes telegram account to stop receiving notifications\n now - get current events \n"
    buttons = [
        [KeyboardButton(messageTypes.NOW)],
        [KeyboardButton(messageTypes.INSTALL),KeyboardButton(messageTypes.REMOVE)],
        # [KeyboardButton(messageTypes.CREDITS)],
        ]
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=message,
                             reply_markup=ReplyKeyboardMarkup(buttons))
        
def install(update, context):
    token = update.effective_chat.id
    text = ""
    if repository.tokenExists(token):
        text = "You are already registered"
    else:
        text = "Registraion successful!"
        repository.addToken(token)
    context.bot.send_message(chat_id=token, text=text)
    
def remove(update, context):
    token = update.effective_chat.id
    text = ""
    if repository.tokenExists(token):
        text = "Unregistered. Sorry to see you go"
        repository.removeToken(token)
    else:
        text = "You are not registered"
    context.bot.send_message(chat_id=token, text=text)
    
def now(update, context):
    token = update.effective_chat.id
    response = eventsService.getNowEvents()
    # response = eventsService.getAllEvents()
    text = ""
    if len(response) == 0:
        text = "There are no events posted right now"
    else:
        for entry in response:
            event = Event(entry)
            text += event.toString() + "\n\n"
    context.bot.send_message(chat_id=token, text=text)
    
def status(update, context):
    token = update.effective_chat.id    
    text = "Number of tokens: {}\n Number of events: {}".format(tokensService.getTokenCount(),eventsService.getPostedEventsCount())
    context.bot.send_message(chat_id=token, text=text)
    
def initTelegram():
    start_handler = CommandHandler("start", start)
    status_handler = CommandHandler("status", status)
    message_handler = MessageHandler(Filters.text, messageHandler)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(status_handler)
    dispatcher.add_handler(message_handler)
    updater.start_polling()

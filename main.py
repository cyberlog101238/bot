import constannce as keys
from telegram.ext import *
import response as R

print("Bot started....")

def start_command(update, context):
    update.message.reply_text('/Help for any help')


def help_command(update, context):
        update.message.reply_text('Hi! Command comming soon..')


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)



def main():
        updater = Updater(keys.token, use_context=True)
        dp = updater.dispatcher

        dp.add_handler(CommandHandler('start', start_command))
        dp.add_handler(CommandHandler('start', help_command))

        dp.add_handler(MessageHandler(Filters.text, handle_message))

        

        updater.start_polling()
        updater.idle()

main()
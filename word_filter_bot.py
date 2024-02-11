

from telegram.ext import Updater, CommandHandler, MessageHandler, filters

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = '6868786051:AAHR7BacaN8Tpq5_WoX8ChDQexrlkucwREc'

# Replace 'bad' with the word you want to filter
FILTER_WORD = 'Stupid','Nigga','Foolish','NOOB','GetSomeSkills'

def start(update, context):
    update.message.reply_text("Hello! I'm your word filter bot. I will filter out the word '{}'. Send me a message to try it out!".format(FILTER_WORD))

def filter_word(update, context):
    message_text = update.message.text.lower()

    # Check if the filter word is present in the message
    if FILTER_WORD in message_text:
        # If present, filter the word and send the filtered message
        filtered_text = message_text.replace(FILTER_WORD, '*' * len(FILTER_WORD))
        update.message.reply_text("Filtered message: {}".format(filtered_text))
    else:
        # If not present, just acknowledge the message
        update.message.reply_text("Message does not contain the filtered word.")



if __name__ == '__main__':
    updater = Updater(TOKEN, True)
    dp = updater.dispatcher


    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(filters.Text & ~filters.Command, filter_word))

    updater.start_polling()
    updater.idle()














































if __name__ == '__main__':
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(filters.text & ~filters.command, filter_word))

    updater.start_polling()
    updater.idle()

""" modules """
from ApiHandlers import start, search_changi, error
from telegram.ext import Updater, CommandHandler
from datetime import datetime
from datetime import timedelta
import time

TOKEN = '1069394752:AAHNOF0oiBrYZ3_IKH7G7gnGVGHI0YP-JP4'

def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('changi', search_changi))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()

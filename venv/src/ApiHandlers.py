from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler

from ChangiQuery import ChangiQuery
from Utils import format_search_res_output

DEBUG_RES_LIST = [{'flight_status': 'Landed', 'estimated_time': '05:19', 'times': '05:40', 'flight_code': 'CX659',
                   'airline': 'CATHAY PACIFIC AIRWAYS'},
                  {'flight_status': 'Landed', 'estimated_time': '11:54', 'times': '11:55', 'flight_code': 'CX691',
                   'airline': 'CATHAY PACIFIC AIRWAYS'},
                  {'flight_status': 'Landed', 'estimated_time': '13:16', 'times': '13:05', 'flight_code': 'CX759',
                   'airline': 'CATHAY PACIFIC AIRWAYS'},
                  {'flight_status': 'Landed', 'estimated_time': '15:19', 'times': '15:40', 'flight_code': 'CX739',
                   'airline': 'CATHAY PACIFIC AIRWAYS'},
                  {'flight_status': 'Confirmed', 'estimated_time': '15:58', 'times': '16:20', 'flight_code': 'CX619',
                   'airline': 'CATHAY PACIFIC AIRWAYS'},
                  {'flight_status': '', 'estimated_time': '', 'times': '18:20', 'flight_code': 'CX735',
                   'airline': 'CATHAY PACIFIC AIRWAYS'},
                  {'flight_status': '', 'estimated_time': '', 'times': '19:15', 'flight_code': 'CX635',
                   'airline': 'CATHAY PACIFIC AIRWAYS'},
                  {'flight_status': '', 'estimated_time': '', 'times': '20:10', 'flight_code': 'CX657',
                   'airline': 'CATHAY PACIFIC AIRWAYS'},
                  {'flight_status': '', 'estimated_time': '', 'times': '23:55', 'flight_code': 'CX715',
                   'airline': 'CATHAY PACIFIC AIRWAYS'}]


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


def search_changi(update, context):
    chat_id = update.message.chat_id
    if context.args[-1] == '1':
        print('debug mode')
        out = format_search_res_output(DEBUG_RES_LIST)
        update.message.reply_text("{}".format('\n'.join(out)))
        # msg = context.bot.send_message(chat_id=chat_id, text="Would you like to set up an alert? (Y/N)")
        # alert(msg, context, chat_id, 60)

    else:
        arrdep = context.args[0]
        airline = str('&'.join(context.args[1:-1]))
        date = context.args[-1]
        out = []

        print('{},{},{}'.format(arrdep, airline, date))

        changi = ChangiQuery(arrdep, search=airline, date=date)

        res_list = changi.search_api()
        print('res list: {} ({} items)'.format(res_list, len(res_list)))

        out = format_search_res_output(res_list)

        update.message.reply_text("{}".format('\n'.join(out)))
        print('done')

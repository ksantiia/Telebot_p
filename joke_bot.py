import telebot
from config import keys_ap, TOKEN
from extensions import PrognozException, Match

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start_help(message: telebot.types.Message):
    text = 'Что может делать этот бот? ' \
           '\nДля получения прогноза введите команду в следующем формате:\n<название матча> ' \
           '\nУвидеть список всех доступных турниров: /leagues'
    bot.reply_to(message, text)

@bot.message_handler(commands=['apl'])
def list_match(message: telebot.types.Message):
    text = 'АПЛ:'
    for key in keys_ap.keys():
        text = '\n'.join((text, key))
    bot.reply_to(message, text)

@bot.message_handler(commands=['leagues'])
def list_leagues(message: telebot.types.Message):
    text = 'Доступные турниры: /apl'
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def get_prognoz(message: telebot.types.Message):
    try:
        values = message.text.lower()

        prog_match = Match.resalt(values)

    except PrognozException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}. '
                              f'Для начала работы введите одну из команд: /start, /help')
    else:

        text = f'{prog_match}'
        bot.send_message(message.chat.id, text)


bot.polling(non_stop=True)
import telebot
import json

bot = telebot.TeleBot('1489262010:AAENU2E27PWX-HswDGVWSGyLuACCOasmcTo')

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
keyboard1.row('Привет', 'Пока', 'Тест')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Пока')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Пфф пока')
    elif message.text.lower() == 'тест':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMsX-cUIHcnAWsC8x8tyavTEg3PwzwAAgoBAALuxKEKkj5OE68x5XgeBA')


@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    json_to_string = str(message)
    a = json_to_string.replace("'", '"')
    b = a.replace("<", '"')
    c = b.replace(">", '"')
    d = c.replace("False", "false")
    e = d.replace("None", "null")
    print(e)
    a1 = json.loads(e)
    A = a1['sticker']['file_id']
    bot.send_message(message.chat.id, f'id этого стикера - {A}')


bot.polling()

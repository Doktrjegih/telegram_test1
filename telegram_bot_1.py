import telebot

bot = telebot.TeleBot('1489262010:AAENU2E27PWX-HswDGVWSGyLuACCOasmcTo')

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Привет', 'Пока')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    elif message.text.lower() == 'оно работает!':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMsX-cUIHcnAWsC8x8tyavTEg3PwzwAAgoBAALuxKEKkj5OE68x5XgeBA')

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)
    bot.send_message(message.chat.id, f'id этого стикера в конце сообщения {message}')

bot.polling()
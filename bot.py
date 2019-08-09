import telebot

bot = telebot.TeleBot("848424096:AAHqU_98gL5Xem6hTpj6H-BbG40xgMAkVNA")

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('🖥 О разработчике', '🛎 Контакты')
keyboard1.row('💡 Услуги', '🌍 Мой сайт')
keyboard1.row('🔥 Как сделать заказ?')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,  'Это демонстрационный бот. Вы можете заказать подобного связавшись со мной', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == '🖥 о разработчике':
        bot.send_message(message.chat.id, 'Привет, меня зовут Юрий и я занимаюсь разработкой Телеграм-ботов Если у вас есть вопросы - свяжитесь со мной! 🔥')
    elif message.text.lower() == '💡 услуги':
        bot.send_message(message.chat.id, 'Создание телеграмм бота для ответа на простые команды\n--Возможность добавления до 5 команд\n--Кастомные клавиатуры\n--Подключение дополнительных функций стороних сайтов(за дополнительную цену)')
    elif message.text.lower() == '🛎 контакты':
        bot.send_message(message.chat.id, 'Email: yura.kachan27@gmail.com\nTelegram: @k_yura13\nInstagram: @yura_k_220')
    elif message.text.lower() == '🔥 как сделать заказ?':
        bot.send_message(message.chat.id, 'Вы можете сделать заказ на одной из бирж\nKwork --https://kwork.ru/script-programming/2120045/sozdam-telegramm-bota ')
    elif message.text.lower() == '🌍 мой сайт':
        bot.send_message(message.chat.id, 'http://okay-site.zzz.com.ua ')

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

bot.polling()
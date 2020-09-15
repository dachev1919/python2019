import telebot
import constants

bot = telebot.TeleBot(constants.token)

#upd = bot.get_updates()

#last_upd = upd[-1]
#message_from_user = last_upd.message

print(bot.get_me())

def log(message, answer):
    from datetime import datetime
    print("--------------")
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \n\tСообщение пользователя - {3}".format(message.from_user.first_name,
                                                                                   message.from_user.last_name,
                                                                                   str(message.from_user.id),
                                                                                   message.text))
    print("\tОтвет Бота - ", answer) 

@bot.message_handler(commands=["start"])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True) #First "True" - Keyboard size, Second - Keyboard disappearance
    user_markup.row('/start', '/stop')
    user_markup.row('фото', 'аудио', 'документы')
    user_markup.row('стикер', 'видео', 'голос', 'локация')
    bot.send_message(message.from_user.id, '(-: Добро пожаловать :-)', reply_markup=user_markup)

@bot.message_handler(commands=["stop"])
def handle_stop(message):
    hide_remove = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, '###', reply_markup=hide_remove)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    print("\n--------------\n", "Message_type 'text'")
    answer = "ООО, прекрасно, вы написали текст!"
    
    if str(message.from_user.id) == "371763121" and message.text.lower() == "привет, бро":
        answer = "Рад вас приветствовать создатель(" + message.from_user.first_name + " " + message.from_user.last_name + ")"
        bot.send_message(message.chat.id, answer)
        log(message, answer)
    elif message.text == "фото":
        print("photo")
    elif message.text.lower() == "привет":
        answer = "Здравствуй."
        log(message, answer)
        bot.send_message(message.chat.id, answer)
    elif message.text.lower() == "пока":
        answer = "Ну пока("
        log(message, answer)
        bot.send_message(message.chat.id, answer)
    elif message.text == "аудио":
        print("User press button 'audio'")
    elif message.text == "документы":
        print("User press button 'documents'")
    elif message.text == "стикер":
        print("User press button 'sticker'")
    elif message.text == "видео":
        print("User press button 'video'")
    elif message.text == "голос":
        print("User press button 'voice'")
    elif message.text == "локация":
        print("User press button 'location'")
    else:
        log(message, answer)
        bot.send_message(message.chat.id, answer)

@bot.message_handler(content_types=["sticker"])
def handle_sticker(message):
    answer = "ЗАЧЕМ ты отправил мне стикер?!"
    print("\n--------------\n", "Message_type 'sticker'")
    bot.send_message(message.chat.id, answer)
    log(message, answer)

@bot.message_handler(content_types=["photo"])
def handle_photo(message):
    answer = "Надеюсь на фотографии не ты)"
    print("\n--------------\n", "Message_type 'photo'")
    bot.send_message(message.chat.id, answer)
    log(message, answer)




bot.polling(none_stop=True, interval=0)
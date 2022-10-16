import telebot

bot=telebot.TeleBot('5713097525:AAF3rGwPMPGOv3VkT1N5br9ayGYminGf8R0')

@bot.message_handler(content_types=['text'])

def get_text_messages(message):
    # Если написали «Привет»
    if message.text == "Привет":
        # Пишем приветствие
      bot.send_message(message.from_user.id,
                         "Привет, сейчас я расскажу тебе гороскоп на сегодня.")
bot.polling(none_stop=True, interval=0)

import pytesseract
from PIL import Image
import telebot;
bot = telebot.TeleBot('KEY');

@bot.message_handler(content_types = ['text'])
def bot_message(message):
    if message.chat.type == 'private':
        bot.send_message(message.chat.id, "Отправьте картинку.")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Отправьте картинку.")

def neiro(name_foto):
        image = Image.open(name_foto)

        string = pytesseract.image_to_string(image, lang='eng')

        mass = ""

        strung_return = string

        print ("\n \n")

        for i in range(1, len(string)):
            if string[i:i+9]=="Microsoft":
                print (string[i:i+9])
                i=i+25
            if string[i] == "-" or string[i-1] == "-" or string[i+1] == "-":
                if string[i+6] == "-" or string[i+5] == "-" or string[i+7] == "-":
                    if string[i+18] == "-" or string[i+17] == "-" or string[i+19] == "-":
                        mass = string[i-6:i+30]
                        break
        print (mass)
        mass_result = mass.replace(" ", "")
        return mass_result, strung_return

@bot.message_handler(content_types=['photo'])
def photo(message):   
     fileID = message.photo[-1].file_id   
     file_info = bot.get_file(fileID)
     downloaded_file = bot.download_file(file_info.file_path)
     with open("image.jpg", 'wb') as new_file:
         new_file.write(downloaded_file)

     mass_result, strung_return = neiro("image.jpg")
     bot.send_message(message.chat.id, mass_result)
     bot.send_message(message.chat.id, strung_return)

bot.polling(none_stop=True, interval=0)

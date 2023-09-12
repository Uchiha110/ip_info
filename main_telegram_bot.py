import telebot

bot = telebot.TeleBot("6017925827:AAHPt6vrOZ7j9u4GSlRvcgPMrVTkYje1KkY")


@bot.message_handler(commands=['start'])
def start(message):
    mess = f"Hi <b>{message.from_user.first_name}</b>!\n" \
           f"Do you need to record ip data, output or maybe delete?\n" \
           f"If you want more information and a list of all commands, type /help"
    bot.send_message(message.chat.id, mess, parse_mode="html")


@bot.message_handler(commands=['write'])
def write(message):
    mess = f"successful"
    bot.send_message(message.chat.id, mess, parse_mode="html")


@bot.message_handler(commands=['select'])
def select(message):
    mess = f"successful"
    bot.send_message(message.chat.id, mess, parse_mode="html")


@bot.message_handler(commands=['server_cleanup'])
def server_cleanup(message):
    mess = f"successful"
    bot.send_message(message.chat.id, mess, parse_mode="html")


@bot.message_handler(commands=['database_cleaning'])
def database_cleaning(message):
    mess = f"successful"
    bot.send_message(message.chat.id, mess, parse_mode="html")


@bot.message_handler(commands=['help'])
def help(message):
    mess = f"All commands inherent in the bot, as well\n" \
           f"as detailed information about the work of the teams:\n" \
           f"/start - I think it's pretty clear what this team does.\n" \
           f"/write - The command obtains an ip address from you and writes it to the database, and then displays data about the ip address you provided.\n" \
           f"/select - The command outputting data about ip addresses, can output data about a particular address, for this you need to enter the name of the column for example id_person and also the id itself with the help of which the rest of the data about the ip address will be output, as well as you can output all the data from the database, when outputting data are output in json files, which you can download.\n" \
           f"/server_cleanup - Cleaning the server where the files are stored.\n" \
           f"/database_cleaning - Cleaning of the database where data on ip addresses is stored.\n" \
           f"/help - This, too, needs no explanation.\n"
    bot.send_message(message.chat.id, mess, parse_mode="html")


bot.polling(none_stop=True)

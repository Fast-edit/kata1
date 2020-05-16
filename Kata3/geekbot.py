from telegram.ext import Updater, CommandHandler

def main():
    updater = Updater (token="1263778590:AAEAxsSncxj4RSZDcMP2HTYScExi0VtZJjM",use_context=True)
    updater.dispatcher.add_handler (CommandHandler("start",start))
    updater.start_polling()
    updater.idle()

def start(update,context):
    update.message.reply_text("Hola soy tu bot")

main()
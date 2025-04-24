import telebot

# Gamitin ang bot token mo
bot = telebot.TeleBot("7922522219:AAEcOZYfrAHQMTmb-5_R64nKBifRn4CvNFg")

# Remove webhook (fix 409 error)
bot.remove_webhook()

print("✅ Webhook removed successfully.")

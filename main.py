import telebot
import os
from config import ADMIN_ID, BOT_TOKEN
from utils import save_pending_email
from email_sender import send_confirmation_email

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, "Hi! Please enter your email address to subscribe:")
    bot.register_next_step_handler(message, save_email)

def save_email(message):
    email = message.text
    if "@" in email and "." in email:
        save_pending_email(email)
        send_confirmation_email(email)
        bot.send_message(message.chat.id, "📩 Confirmation email sent! Please check your inbox.")
    else:
        bot.send_message(message.chat.id, "Invalid email. Please try again.")

@bot.message_handler(commands=['listemails'])
def list_emails(message):
    if message.from_user.id == int(ADMIN_ID):
        with open("confirmed_emails.txt", "r") as f:
            emails = f.read()
        bot.send_message(message.chat.id, f"✅ Confirmed Emails:\n{emails}")
    else:
        bot.send_message(message.chat.id, "Unauthorized.")

bot.polling()

import telebot


TOKEN = "*"
chat_id = '*'
tb = telebot.TeleBot(TOKEN)
login_data = {
    'username': '*',
    'password': '*'
}
login_url = 'https://www.tesmanian.com/account'

def bot_send_message(chat_id, data ):
    tb.send_message(chat_id, data )

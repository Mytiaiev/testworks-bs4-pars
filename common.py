import telebot


TOKEN = "5457793866:AAGvpAkj0h6wYKoJNMpQiLgmjU6DpVMqEVE"
chat_id = '-619051510'
tb = telebot.TeleBot(TOKEN)
login_data = {
    'username': 'mytiaievqa@gmail.com',
    'password': 'qwerty=1'
}
login_url = 'https://www.tesmanian.com/account'

def bot_send_message(chat_id, data ):
    tb.send_message(chat_id, data )
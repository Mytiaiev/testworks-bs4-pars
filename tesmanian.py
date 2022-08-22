from bs4 import BeautifulSoup as bs
import requests
import telebot
import time

TOKEN = "*"
chat_id = '*'
tb = telebot.TeleBot(TOKEN)
login_data = {
    'username': '*',
    'password': '*'
}
login_url = 'https://www.tesmanian.com/account'
  
def bot_send_message(chat_id:str, data:str ):
    tb.send_message(chat_id, data ) 
    
def pars_page(url: str):
    allNews = []
    try:
        page = requests.get(url)
        soup.find('span', 'login')
        request.get('https://www.tesmanian.com/account')
        with requests.Session() as s:
            response = requests.post(login_url , login_data)
    except:
        while True:
            page = requests.get(url)
            soup = bs(page.text, 'html.parser')
            parse = soup.findAll('h2')
            for i in parse:
                if i not in allNews:
                    links = i.find('a').get('href')
                    allNews.append(i)
                    bot_send_message(chat_id, (i.text+f' https://www.tesmanian.com/{links}' ))
                else:
                    bot_send_message(chat_id, ('nothing new'))              
        time.sleep(15)
                
        
pars_page('https://www.tesmanian.com/blogs/tesmanian-blog')

       

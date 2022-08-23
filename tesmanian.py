from bs4 import BeautifulSoup as bs
from common import *
import requests
import time

class ParsingNewTitle():
    def __init__(self, url) -> None:
        self.url = url
        
    def pars_page(url):
        allNews = []
        while True:
            try:
                page = requests.get(url)
                soup.find('span', 'login')
                requests.get('https://www.tesmanian.com/account')
                with requests.Session() as s:
                    response = requests.post(login_url , login_data)
            except:
                page = requests.get(url)
                soup = bs(page.text, 'html.parser')
                parse = soup.findAll('h2')
                for title in parse:
                    if title not in allNews:
                        link = title.find('a').get('href')
                        print(title.text)
                        print(f'https://www.tesmanian.com/{link}')
                        allNews.append(title)
                        bot_send_message(chat_id, (title.text+f' https://www.tesmanian.com/{link}' ))
                    else:
                        print('nothing new')
                        break
            time.sleep(15)
        
        
            
            
ParsingNewTitle.pars_page('https://www.tesmanian.com/blogs/tesmanian-blog')

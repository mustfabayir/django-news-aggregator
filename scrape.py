from bs4 import BeautifulSoup as soup
import requests
import json
import sqlite3
import random
from datetime import datetime
#from fake_useragent import UserAgent

class GetNewsLink:
    def __init__(self):
        self.url = 'https://www.foxnews.com/us'
        self.links = []
    
    def get_source_code(self):
        r = requests.get(self.url)
        if(r.status_code == 200):
            self.scraping_process(r.content)
        return self.links

    def scraping_process(self, context):
        b = soup(context, 'html.parser')
        self.us_news_link(b)
        

    def us_news_link(self, b):   
        links = b.find_all('h4', class_='title')
        for link in links:
            c = link.find('a')
            href = c.get('href')
            if (href[0] != 'h'):
                full_url = 'https://www.foxnews.com' + href
                self.links.append(full_url)
                


class GetNewsDetails:
    def __init__(self, url):
        self.url = url
        self.connection = sqlite3.connect('fox_news/db.sqlite3')
        self.cursor = self.connection.cursor()
        self.details = {}

    def get_source_code(self):
        r = requests.get(url)
        if(r.status_code == 200):
            self.scraping_process(r.content)
            self.convert_to_json(self.details)
        
    def scraping_process(self, context):
        b = soup(context, 'html.parser')
        self.get_news_details(b)


    def convert_to_json(self, dict_data):
        converted_data = json.dumps(dict_data)
        self.save_to_database(converted_data)
        

    def save_to_database(self, converted_data):
        randomNumber = random.randint(1,1000)
        id = int(datetime.now().microsecond)+randomNumber
        self.connection.execute('insert into news_app_newsdetails values(?,?)',[id,converted_data])
        self.connection.commit()

    def get_news_details(self, b):
        title = b.find('h1', class_="headline").text
        news_image = b.find('div', class_="m").find('img').get('src')
        self.details = {'title': title, 'news_image': news_image, 'content':[]}
        
        # try:
        #     news_image = soup.find('div',attrs={"class":"m"}).find('img').get('src')
        #     print(news_image)
        # except:
        #     pass
        article_body = b.find('div', class_="article-body").find_all('p')
        for details in article_body:
            try:
                texts = details.text
                self.details['content'].append({'texts': texts})
                #print(texts)
            except:
                pass
            try:
                related_links = details.find('a')
                related_links_href = related_links.get('href')
                self.details['content'].append({'related_links_href': related_links_href})
                #print(related_links_href)
            except:
                pass


links = GetNewsLink().get_source_code()

for url in links:
    GetNewsDetails(url).get_source_code()
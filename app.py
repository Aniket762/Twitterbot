from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Twitterbot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()
        
    def login(self):
        bot = self.bot
        bot.get('https://twitter.com')
        time.sleep(10)


ed = Twitterbot('username','password')

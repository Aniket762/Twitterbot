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
        email = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)


    def like_tweet(self,hastag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hastag+'&src=typd')
        time.sleep(3)



ed = Twitterbot('username','password')
ed.login()
ed.like_tweet('hackathon')

from selenium import webdriver
from time import sleep

CHROME_DRIVER_PATH = '/home/msmickersgill/metabot-docker/chromedriver'
INSTA_EMAIL = 'mariasmickersgill@live.com'
INSTA_PASSWORD = 'rosebud22'
ACCOUNT_TO_SCRAPE = 'https://www.instagram.com/reductress/'

class InstaFollowers: 
    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self): 
        self.driver.get('https://www.instagram.com/')
        sleep(2)
        username = self.driver.find_element_by_xpath('//input[@name="username"]')
        username.send_keys(INSTA_EMAIL)
        password = self.driver.find_element_by_xpath('//input[@name="password"]')
        password.send_keys(INSTA_PASSWORD)
        self.driver.find_element_by_xpath('//button/div[text()="Log In"]').click()
        sleep(5)

    def find_followers(self): 
        self.driver.get('https://www.instagram.com/reductress/')
        sleep(3)
        self.driver.find_element_by_xpath('//a[text()=" followers"]').click()
        for account in len(self.driver.find_elements_by_xpath('//div[@aria-label="Followers"]//li')): 
            self.follow()
        self.driver.quit()

    def follow(self): 
        self.driver.find_element_by_xpath('//button[text()="Follow"]')

bot = InstaFollowers(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
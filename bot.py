from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep, strftime
from random import randint
import configparser
from selenium.webdriver.common.action_chains import ActionChains
#import pandas as pd

"""
#chromedriver_path = '/Users/williamsprouse/Desktop/WAVEX/Auto Insta/chromedriver' # Change this to your own chromedriver path!
#webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

config = configparser.ConfigParser()
config.read('../config.ini')

username = webdriver.find_element_by_name('username')
username.send_keys(config['CREDENTIALS']['username'])
password = webdriver.find_element_by_name('password')
password.send_keys(config['CREDENTIALS']['password'])

try:

    button_login = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div')
    button_login.click()

    sleep(8)

    #button_dontSavePassword = webdriver.find_element_by_xpath('./section/main/div/div/div/section/div/button')
    #button_dontSavePassword.click()
    #sleep(8)

    button_notifications = webdriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
    button_notifications.click()
    #sleep(8)

    #notnow = webdriver.find_element_by_css_selector('body > div:nth-child(13) > div > div > div > div.mt3GC > button.aOOlW.HoLwm')
    #notnow.click() #comment these last 2 lines out, if you don't get a pop up asking about notifications

except:
    pass
    #webdriver.close()
    #Test

"""
class InstagramRobot:

    def __init__(self, chromedriverPath, config):
        self.driver = webdriver.Chrome(executable_path=chromedriverPath)

        self.config = configparser.ConfigParser()
        self.config.read(config)

        self.username = self.config['CREDENTIALS']['username']
        self.password = self.config['CREDENTIALS']['password']

    def start(self):
        webdriver = self.driver
        sleep(2)
        webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        sleep(3)

    def login(self):
        username = self.driver.find_element_by_name('username')
        username.send_keys(self.username)
		
        password = self.driver.find_element_by_name('password')
        password.send_keys(self.password)

        sleep(1)

        button_login = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div')
        button_login.click()

        sleep(3)

        button_dontSavePassword = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        button_dontSavePassword.click()
        sleep(3)

        button_notifications = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        # 							  /html/body/div[3]/div/div/div/div[3]/button[2]
        # 							  /html/body/div[3]/div/div/div/div[3]/button[2]
        # 							  /html/body/div[3]/div/div/div/div[3]/button[2]
        button_notifications.click()
        sleep(3)

    def search(self, username):
        #search_bar = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div/div/span[2]')
        search_bar = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div/div/span[2]')
        search_bar.click()
        sleep(1)

        search_bar2 = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search_bar2.send_keys(username)

        sleep(4)

        click_user = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]/div/div[2]/div/span')
        click_user.click()
        #search_bar2.submit()

    def follow(self, username):
        self.search(username)
        sleep(4)
        follow_button = self.driver.find_elements_by_xpath("//*[contains(text(), 'Follow')]")
        follow_button[0].click()
		
    def unfollow(self, username):
        """Must be following the user, and must be on the users page. Call search() method before this method."""
        #unfollow_button = self.driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[2]/div[2]/span/span[1]/button')
        #sleep(3)
        #unfollow_button = self.driver.find_elements_by_xpath("//*[contains(text(), 'Following')]")
        #unfollow_button = self.driver.find_element_by_name("Following")
        #unfollow_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[2]/div[2]/span/span[1]/button/div/span')

        #actions = ActionChains(self.driver)
        #actions.move_to_element_with_offset(self.driver.find_element_by_tag_name('body'), 0,0)
        #actions.move_by_offset(762, 274).click().perform()
  
        #print(unfollow_button)
        unfollow_button = self.driver.find_element(By.XPATH, '//button[text()="Following"]')
        unfollow_button.click()
         



pass

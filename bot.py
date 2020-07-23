from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep, strftime
from random import randint
import configparser
from selenium.webdriver.common.action_chains import ActionChains
#import pandas as pd


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

        unfollow_button = self.driver.find_element_by_class_name('glyphsSpriteFriend_Follow.u-__7')
        unfollow_button.click()

        sleep(1)
        

        unfollow_confirm_button = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[1]')
        unfollow_confirm_button.click()         
        sleep(2)



pass

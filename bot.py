from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import configparser
#import pandas as pd

chromedriver_path = '/Users/williamsprouse/Desktop/WAVEX/Auto Insta/chromedriver' # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
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
    sleep(3)

    notnow = webdriver.find_element_by_css_selector('body > div:nth-child(13) > div > div > div > div.mt3GC > button.aOOlW.HoLwm')
    notnow.click() #comment these last 2 lines out, if you don't get a pop up asking about notifications

except:
    pass
    webdriver.close()


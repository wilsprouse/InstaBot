from bot import InstagramRobot
from time import sleep

#print("starting")
insta = InstagramRobot('/Users/williamsprouse/Desktop/WAVEX/AutoInsta/chromedriver', '../config.ini')
insta.start()
insta.login()

insta.scrollHashtag('coding', 2)


'''
follow_list = ["the_intelligent.investor", "acorns", "your_first_million", "thebusinesshacks", "themotleyfoolofficial", "_investing", "startupbosss","bullishsecurities", "investopedia", "nasdaq"]

for i in follow_list:
	insta.follow(i)

for i in follow_list:
        insta.follow(i)

cnt = 0
hashtags = ['learntotrade', 'tradingtech','wealthmanagement']
for i in hashtags:
    insta.scrollHashtag(i, 500)
    print("Done")
    #cnt += 1
    #if (cnt%10 == 0):
        print(cnt)
'''

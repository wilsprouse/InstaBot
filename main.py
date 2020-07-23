from bot import InstagramRobot
from time import sleep

insta = InstagramRobot('/Users/williamsprouse/Desktop/WAVEX/AutoInsta/chromedriver', '../config.ini')
insta.start()
insta.login()
#insta.search("_codehub_")
#insta.unfollow("_codehub_")
#insta.follow("_codehub_")


follow_list = ["_codehub_", "programmerplus"]

for i in follow_list:
	insta.follow(i)

#sleep(10)
#for i in follow_list:
#	insta.search(i)
#	insta.unfollow(i)

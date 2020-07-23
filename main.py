from bot import InstagramRobot
from time import sleep

insta = InstagramRobot('/Users/williamsprouse/Desktop/WAVEX/AutoInsta/chromedriver', '../config.ini')
insta.start()
insta.login()
#insta.search("coding")
#insta.unfollow("_codehub_")
#insta.follow("_codehub_")
insta.scrollHashtag("coding", 1)


follow_list = ["_codehub_", "programmerplus"]

for i in follow_list:
	pass #insta.follow(i)

#sleep(10)
#for i in follow_list:
#	insta.search(i)
#	insta.unfollow(i)

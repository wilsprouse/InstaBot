from bot import InstagramRobot
from time import sleep

#print("starting")
insta = InstagramRobot('/Users/williamsprouse/Desktop/WAVEX/AutoInsta/chromedriver', '../config.ini')
insta.start()
insta.login()
#insta.search("coding")
#insta.unfollow("_codehub_")
#insta.follow("_codehub_")
insta.scrollHashtag("stockpick", 250)
#insta.comment("great post")

print("Done!")


'''
follow_list = ["lets.coding", "cifertech", "programunity", "hackers.pg", "misscod3r", "thedevlife", "codinggoats",
		"comment_sense", "raspizone", "codingwitharman", "hacksterio", "codingdays", "peoplewhocode",
		"dancode_js", "codehub.py"]

for i in follow_list:
	insta.follow(i)
'''
#sleep(10)
#for i in follow_list:
#	insta.search(i)
#	insta.unfollow(i)

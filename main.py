from bot import InstagramRobot

insta = InstagramRobot('/Users/williamsprouse/Desktop/WAVEX/AutoInsta/chromedriver', '../config.ini')
insta.start()
insta.login()
#insta.search("_codehub_")
insta.follow("__codehub_")

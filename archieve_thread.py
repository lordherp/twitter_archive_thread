# This snippet pulls out all the tweet ids from a thread
# Input --> ID of last tweet in thread ; Output --> all the tweet ids
# We load our config from an object, or module (config.py)

import tweepy
from config import access_token, access_secret, consumer_key, consumer_secret
from subprocess import call

# app.config and database location
# These config variables come from 'config.py'
# put your db file path here e.g C:\\projects\\blah\\blah\\xyz.db (I use windows so the path has \\ , if you use unix change accordingly)

database_loc = 'C:\\abc\\def\\database.db'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

last_tweet_in_thread = input(
    "Enter the last tweet in thread which you want saved: ")

status_object = api.get_status(last_tweet_in_thread)

tweets_to_save = [last_tweet_in_thread]

while status_object.in_reply_to_status_id_str is not None:
    reply_tweet_id = status_object.in_reply_to_status_id_str
    print("Tweets to fetch : " + reply_tweet_id)
    tweets_to_save.append(reply_tweet_id)
    status_object = api.get_status(reply_tweet_id)
command_string = 'twitter-to-sqlite.exe ' + 'statuses-lookup ' + \
    database_loc + ' ' + \
    ' '.join(map(str, tweets_to_save)) + ' ' + '--skip-existing'

try:
    call(command_string)
    print("Fetch completed successfully!")
except Exception as e:
    raise e

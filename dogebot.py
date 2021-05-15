import os
import datetime
import schedule
import time
from dotenv import load_dotenv
from binance import Client
import tweepy

from analyse_tweet import analyse_tweet

load_dotenv()

# Api Keys
binance_api_key = os.getenv('BINANCE_API')
binance_api_secret = os.getenv('BINANCE_SECRET')
twitter_api_key = os.getenv('CONSUMER_KEY')
twitter_api_secret = os.getenv('CONSUMER_SECRET')
twitter_api_token = os.getenv('ACCESS_TOKEN')
twitter_api_secret_token = os.getenv('ACCESS_TOKEN_SECRET')

# Binance API
client = Client(binance_api_key, binance_api_secret)

# Twitter API
auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_secret)
auth.set_access_token(twitter_api_token, twitter_api_secret_token)
twitter_api = tweepy.API(auth, wait_on_rate_limit=True)

# #
#   Check for new tweets
# #


def checkForNewTweet(twitter_api):
    tweets = twitter_api.user_timeline(
        screen_name="evalo01",
        count=1,
        lang="en",
        tweet_mode="extended",
        include_rts=False,
    )[0]

    # Tweet text
    tweet = tweets.full_text

    # Parse Tweet
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    no_punct = ""

    for char in tweet:
        if char not in punctuations:
            no_punct = no_punct + char

    tweet = no_punct

    # Get the minute since tweet
    time_difference = datetime.datetime.now().minute - tweets.created_at.minute

    # If tweet is less than 3 min old, analyse and buy
    if time_difference <= 3 or time_difference == 0:
        analyse_tweet(tweet, client)
    else:
        return


if __name__ == "__main__":
    schedule.every(10).seconds.do(checkForNewTweet, twitter_api)

    while 1:
        schedule.run_pending()
        time.sleep(1)

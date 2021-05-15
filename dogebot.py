import os
import datetime
from dotenv import load_dotenv
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
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

# Twitter API
auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_secret)
auth.set_access_token(twitter_api_token, twitter_api_secret_token)
twitter_api = tweepy.API(auth, wait_on_rate_limit=True)

# #
#   Twitter Functions
# #

# Working with Doge devs to improve system transaction efficiency. Potentially promising.
# To be clear, I strongly believe in crypto, but it can’t drive a massive increase in fossil fuel use, especially coal
# Do you want Tesla to accept Doge?


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

    # Get the minute since tweet
    time_difference = datetime.datetime.now().minute - tweets.created_at.minute

    # If tweet is less than 3 min old, analyse and buy
    if time_difference <= 3 or time_difference == 0:
        analyse_tweet(tweet)
    else:
        analyse_tweet(tweet)


# #
#   Binance API
# #


client = Client(binance_api_key, binance_api_secret)


def buyDoge(client):
    # Get DOGE price
    doge_price = client.get_symbol_ticker(symbol="DOGEUSDT")

    # Calculate how much DOGE $25 can buy
    buy_quantity = round(25 / float(doge_price['price']))

    # Create & Process Order
    order = client.create_test_order(
        symbol='DOGEUSDT',
        side=Client.SIDE_BUY,
        type=Client.ORDER_TYPE_MARKET,
        quantity=buy_quantity
    )

    print(doge_price, buy_quantity)


checkForNewTweet(twitter_api)

from textblob import TextBlob
from binance import Client
from binance.enums import *
import time

# #
#   Binance Order
# #


def doge_order_request(client):
    # Get DOGE price
    doge_price = client.get_symbol_ticker(symbol="DOGEUSDT")

    # Calculate how much DOGE $25 can buy
    buy_quantity = round(25 / float(doge_price['price']))

    # Create & Process Order
    try:
        client.create_order(
            symbol='DOGEUSDT',
            side=Client.SIDE_BUY,
            type=Client.ORDER_TYPE_MARKET,
            quantity=buy_quantity
        )
        print('Bought', buy_quantity, 'DOGE at', doge_price['price'])
        print('Cooling down for 4 minutes')

        time.sleep(240)
    except:
        return


def analyse_tweet(tweet, client):
    # #
    # Get Tweet Polarity
    # #
    blob = TextBlob(tweet)
    total_polarity = 0
    num_of_sentences = 0

    # For each sentence...
    for sentence in blob.sentences:
        # Add the sentence polarity to total_polarity
        total_polarity = total_polarity + sentence.sentiment.polarity

        # Increment sentences
        num_of_sentences += 1

    # Get average polarity
    avg_polarity = total_polarity / num_of_sentences

    # #
    # Check Tweet Keywords
    # #
    keywords = ['doge', 'dogecoin', 'crypto']
    tweet_keywords = tweet.lower().split()

    # Check if tweet contains and keywords
    if any(keywords in tweet_keywords for keywords in keywords):

        # If avg_polarity is less than or equal to zero, order.
        if avg_polarity >= 0:
            doge_order_request(client)
        else:
            return
    else:
        return

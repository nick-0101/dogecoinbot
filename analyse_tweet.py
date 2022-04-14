from textblob import TextBlob
from binance import Client
from binance.enums import *
import time

# Functions
from handle_transactions import doge_order_request


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
    if any(keywords in tweet_keywords for keywords in keywords) and avg_polarity >= 0:
        # Log
        print('Tweet contains a positive sentiment of dogecoin.')

        # Send a doge order request
        doge_order_request(client)
    else:
        return

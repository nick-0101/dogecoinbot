from textblob import TextBlob


def analyse_tweet(tweet):
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
    print(avg_polarity)

    # #
    # Check Tweet Keywords
    # #
    # keywords = ['doge', 'dogecoin', 'crypto']
    tweet_keywords = tweet.lower().split()

    print(tweet_keywords)

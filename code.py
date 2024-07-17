# Twitter Sentiment Analysis
import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
import nltk
# download nltk using the Command promt : python -m textblob.download_corpora

# 1. Authentications
def authenticate_twitter(consumer_key, consumer_secret, access_token, access_token_secret):
    """
    Authenticate with Twitter API.
    
    Args:
    consumer_key (str): Twitter API consumer key
    consumer_secret (str): Twitter API consumer secret
    access_token (str): Twitter API access token
    access_token_secret (str): Twitter API access token secret
    """
    try:
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        return api
    
    except:
        print("Error: Authentication Failed")
        return None
# 2. cleaning tweet  
def clean_tweet(tweet):
    """
    cleaning by removing links, special characters
    """
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\s+)", " ",tweet).split())

# 3. sentiment analysis

def get_tweet_sentimet(tweet):
    """
    tweet(str): tweet text to analyze
    Returns:
    sentiment of the tweet ('positive', 'neutral', or 'negative')
    """
    
    analysis = TextBlob(clean_tweet(tweet))
    if analysis.sentiment.polarity > 0:
        return 'positive'
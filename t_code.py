import re
import asyncio
from textblob import TextBlob
from twikit import Client

async def clean_tweet(tweet):
    """
    Clean tweet text by removing links, special characters using regex.
    """
    return ' '.join(re.sub(r"(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

async def get_tweet_sentiment(tweet):
    """
    Classify sentiment of passed tweet using TextBlob's sentiment method.
    """
    analysis = TextBlob(await clean_tweet(tweet))
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'

async def get_tweets(client, query, count=10):
    """
    Fetch tweets and parse them.
    """
    print(f'My search and analysis key word : {query}')
    tweets = []
    try:
        fetched_tweets = await client.search_tweet(query, 'Latest', count)
        for tweet in fetched_tweets:
            parsed_tweet = {}
            parsed_tweet['text'] = tweet.text
            parsed_tweet['sentiment'] = await get_tweet_sentiment(tweet.text)
            tweets.append(parsed_tweet)
        return tweets
    except Exception as e:
        print(f"Error : {str(e)}")
        return []

async def analyze_tweets(tweets):
    """
    Analyze tweets and print statistics.
    """
    if not tweets:
        print("No tweets were retrieved. Please check your query and try again.")
        return

    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    
    print(f"Positive tweets percentage: {100*len(ptweets)/len(tweets):.2f}%")
    print(f"Negative tweets percentage: {100*len(ntweets)/len(tweets):.2f}%")
    print(f"Neutral tweets percentage: {100*(len(tweets) - (len(ntweets) + len(ptweets)))/len(tweets):.2f}%")
    
    print("\n\nPositive tweets:")
    for tweet in ptweets[:5]:
        print(tweet['text'])
    
    print("\n\nNegative tweets:")
    for tweet in ntweets[:5]:
        print(tweet['text'])
        
        
async def main():
    # Initialize client
    client = Client('en-US')
    
    # Login to Twitter
    await client.login(
        auth_info_1='username or email',
        auth_info_2='YOUR_EMAIL_OR_PHONE',
        password='your password'
    )
    
    try:
        # Get tweets
        tweets = await get_tweets(client, query='Machine Learning', count=100)
        
        
        if tweets:
            # Analyze tweets
            await analyze_tweets(tweets)
        else:
            print("No tweets were retrieved. Please check your query and try again.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())
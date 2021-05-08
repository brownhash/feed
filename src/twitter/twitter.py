import tweepy
import os

# -----------------------------------------------------------------------------
# initiate the class with following values
# -----------------------------------------------------------------------------
# consumer_key = "xxxxxxxxxxxxxx"
# consumer_secret = "xxxxxxxxxxxxxx"
# access_token = "xxxxxxxxxxxxxx"
# access_token_secret = "xxxxxxxxxxxxxx"
#
# -----------------------------------------------------------------------------
# or set the following equivalent environement variables
# -----------------------------------------------------------------------------
# TWITTER_CONSUMER_KEY="xxxxxxxxxxxxxx"
# TWITTER_CONSUMER_SECRET="xxxxxxxxxxxxxx"
# TWITTER_ACCESS_TOKEN="xxxxxxxxxxxxxx"
# TWITTER_ACCESS_TOKEN_SECRET="xxxxxxxxxxxxxx"
class Twitter(object):
    def __init__(self, consumer_key=None, consumer_secret=None, access_token=None, access_token_secret=None):
        self.consumer_key = consumer_key if consumer_key else os.environ['TWITTER_CONSUMER_KEY']
        self.consumer_secret = consumer_secret if consumer_secret else os.environ['TWITTER_CONSUMER_SECRET']
        self.access_token = access_token if access_token else os.environ['TWITTER_ACCESS_TOKEN']
        self.access_token_secret = access_token_secret if access_token_secret else os.environ['TWITTER_ACCESS_TOKEN_SECRET']

    # Initiate tweepy client with above provided credentials
    def __client(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        api = tweepy.API(auth)

        return api

    # use the initiated client to post a tweet
    def make_tweet(self, tweet):
        tweet_type = type(tweet).__name__
        if tweet_type == 'str':
            tweet_len = len(tweet)
            if tweet_len <= 280:
                return self.__client().update_status(status=tweet)
            else:
                raise Exception('tweet exceeds the twitter limit of 280 chars by `{}` chars'.format(tweet_len-280))
        else:
            raise Exception('tweet can only be a string value and not `{}`'.format(tweet_type))

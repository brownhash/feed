from twitter.twitter import Twitter

# -----------------------------------------------------------------------------
# set post_data value to be
# -----------------------------------------------------------------------------
# {
#     "post_type": ["tweet"],
#     "content": "Hello world!"
# }
# post_type could be multiple values, currently supported is tweet
# content will impose character limit on it according to the platform 
# eg; twitter allows a tweet to be of maximum 280 chars
class MakePost(object):
    def __init__(self, post_data):
        # these responses will help create analytics stream
        response_aggregator = []

        if 'tweet' in post_data['post_type']:
            response = self.__make_tweet(content=post_data['content'])
            response_aggregator.append(response)

    def __make_tweet(self, content):
        twitterClient = Twitter()

        tweet_data = twitterClient.make_tweet(tweet=content)._json

        return {
            'created_at': tweet_data['created_at'],
            'url': 'https://twitter.com/{username}/status/{tweet_id}'.format(
                username=tweet_data['user']['screen_name'], 
                tweet_id=tweet_data['id'])
        }

"""
Module that contains simple in memory storage implementation
"""


class Storage(object):

    _tweets = []
    server_id = "felna"
    tweet_count: 0

    @classmethod
    def get_tweets(cls):
        """
        Method used to return all tweets
        """
        return cls._tweets

    @classmethod
    def get_tweet(cls, tweet_id):
        """
        Method used to return single tweet
        """
        for tweet in cls._tweets:
            if tweet['id'] == tweet_id:
                return tweet
        else:
            return None

    @classmethod
    def add_tweet(cls, _tweet_id, name, tweet):
        """
        Method used to return add tweet
        """
        cls._tweets.append({'id': id, 'name': name, 'tweet': tweet})

"""
Module that contains simple in memory storage implementation
"""


class Storage(object):
    _tweets = []

    @classmethod
    def get_tweets(cls):
        return cls._tweets

    @classmethod
    def get_tweet(cls, tweet_id):
        for tweet in cls._tweets:
            if tweet['id'] == tweet_id:
                return tweet
        else:
            return None

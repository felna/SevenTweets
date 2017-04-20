"""
Module that contains simple in memory storage implementation
"""

class Storage(object):

    _tweets = []

    @classmethod
    def get_tweets(cls):
        return cls._tweets

    @classmethod
    def get_tweet(cls,tweet_id):
        for tweet in cls._tweets:
            if tweet['id'] == tweet_id:
                return tweet
        else:
            return None

    @classmethod
    def add_tweet(cls,id,name,tweet):
        cls._tweets.append({'id':id,'name':name,'tweet':tweet})
"""
Module that contains simple in memory storage implementation
"""


class Storage(object):

    _tweets = []
    server_name = "felna"
    _tweet_count: 0

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
    def post_tweet(cls, body):
        cls._tweet_count += 1
        tweet = {"id": cls._tweet_count,"name": "Milos", "tweet": body}
        cls._tweets.append(tweet)
        return "Ok"

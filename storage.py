class Storage(object):
    _tweets = []
    _tweet_count  = 0
    server_name = "felna"

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
    def post_tweet(cls, body):
        cls._tweet_count += 1
        tweet = {"id": cls._tweet_count,"name": cls.server_name, "tweet": body}
        cls._tweets.append(tweet)
        return "Ok"

    @classmethod
    def del_tweet(cls, tweet_id):

        for tweet in cls._tweets:
            if tweet['id'] == tweet_id:
                del cls._tweets[cls._tweets.index(tweet)]
            else:
                raise IndexError ("No tweet with index {}".format(tweet_id))
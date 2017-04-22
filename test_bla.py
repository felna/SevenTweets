from storage import Storage


def test_success():
    return True


def test_tweets_get():
    Storage._tweets.clear()
    Storage._tweets.append(12)
    assert Storage.get_tweets() == [12]

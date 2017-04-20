import requests
import json

url = "http://127.0.0.1:5000/tweets/"

r = requests.post(
    url,
    json = json.dumps({'tweet': 'Hello world_1!'})
)
"""
r = requests.post(
    url,
    json = json.dumps({'tweet': "Hello world_2!"})
)
r = requests.post(
    url,
    # json = json.dumps({'tweet': ""})
)
tweet_id = 2
r = requests.get("{}{}".format(url, tweet_id))
print("tweet ({}): ".format(tweet_id), r.text)
tweet_id = 1
r = requests.delete("{}{}".format(url, tweet_id))
"""
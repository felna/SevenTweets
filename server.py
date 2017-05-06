from flask import Flask, request
import json
from flask import jsonify
from storage import Storage

app = Flask(__name__)


@app.route("/tweets/", methods=["GET"])
def get_tweets():
    """
    Server reaction to /tweet route
    """
    tweet = Storage.get_tweets()
    return jsonify(Storage.get_tweets()) if tweet else ("No tweets", 404)


@app.route("/tweets/<int:tweet_id>", methods=["GET"])
def get_tweet(tweet_id):
    """
    Server reaction to /tweet/tweet_id route bla
    """
    tweet = Storage.get_tweet(tweet_id)
    return jsonify(tweet) if tweet else ("Not found", 404)


@app.route("/tweets/", methods=["POST"])
def post_tweet():
    """
    Server reaction to /tweets/ using POST method
    """
    if not request.get_json():
        return ("Missing tweet", 400)
    tweet = Storage.post_tweet(json.loads(request.get_json())["tweet"])
    return (jsonify(tweet),201)

@app.route("/tweets/<int:tweet_id>", methods=['DELETE'])
def del_tweet(tweet_id):

    """
    Server reaction to /tweets/ using DELETE method
    """
    return (jsonify(Storage.del_tweet(tweet_id)), 204)


if __name__ == "__main__":
    app.run(host='0.0.0.0')

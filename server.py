from flask import Flask, request
from flask import jsonify
from storage import Storage

app = Flask(__name__)


@app.route("/tweets/", methods=["GET"])
def get_tweets():
    """
    Server reaction to /tweet route
    """
    return jsonify(Storage.get_tweets())


@app.route("/tweets/<int:tweet_id>", methods=["GET"])
def get_tweet(_tweet_id):
    """
    Server reaction to /tweet/tweet_id route
    """
    tweet = Storage.get_tweets(_tweet_id)


@app.route("/tweets/", methods=["POST"])
def post_tweet():
    """
    Server reaction to /tweets/ using POST method
    """
    body = request.data
    print(body)


if __name__ == "__main__":
    app.run()

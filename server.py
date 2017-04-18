from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello world!"


@app.route("/poster/", methods=["POST"])
def poster():
    print(request.json)
    print(request.headers)
    return "Hello world!"


@app.route("/hello/<username>")
def hello_name(username):
    return "Hello " + username + "!"


if __name__ == "__main__":
    app.run()

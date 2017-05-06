from fabric.api import local, env

env.host = ["finally.sedamcvrkuta.com"]
env.user = "root"

name = "SevenTweets"
port = 8000
repository = "SevenTweets"
network = "radionica_test"


def build(tag=""):
    if tag is not "":
        tag = ":" + tag
    local(f"docker build -t {repository}{tag} .")


def create_network():
    local(f"docker network crate {network}")
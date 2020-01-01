import requests
from flask import Flask, request

app = Flask(__name__)

TOKEN = '1069394752:AAHNOF0oiBrYZ3_IKH7G7gnGVGHI0YP-JP4'


def get_url(method):
    return "https://api.telegram.org/bot{}/{}".format(TOKEN, method)


@app.route("/{}".format(TOKEN), methods=["POST"])
def process_update():
    if request.method == "POST":
        update = request.get_json()
        return "ok!", 200

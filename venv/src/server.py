import requests
from flask import Flask, request

app = Flask(__name__)

TOKEN = '1069394752:AAHNOF0oiBrYZ3_IKH7G7gnGVGHI0YP-JP4'


def get_url(method):
    return "https://api.telegram.org/bot{}/{}".format(TOKEN, method)


def process_message(update):
    data = {"chat_id": update["message"]["from"]["id"], "text": "I can hear you!"}
    r = requests.post(get_url("sendMessage"), data=data)


@app.route("/{}".format(TOKEN), methods=["POST"])
def process_update():
    if request.method == "POST":
        update = request.get_json()
        if "message" in update:
            process_message(update)
        return "ok!", 200

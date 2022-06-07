import os
from unicodedata import name
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from datetime import datetime

app = App(token=os.environ.get("SLACK BOLT TOKEN"))

@app.message(":wave:")
def say_hello(message, say):
    user = message['user']
    say(f"Hi, there, <@{user}>!")


if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK APP TOKEN"]).start()
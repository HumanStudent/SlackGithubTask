import os
from flask import Flask
from flask import request
from flask import json
from github_webhook import Webhook
from github import Github
from pathlib import Path
from dotenv import load_dotenv
from slack import WebClient


app = Flask(__name__)
webhook = Webhook(app) # Defines '/postreceive' endpoint

# @app.route('/', methods=['GET', 'POST'])
# def homepage():
#     return "test 123456879"

# @app.route('/', methods=['GET'])
@app.route('/')
def get_github_payload():
    if request.headers['Content-Type'] == 'application/json':
        data = json.dumps(request.json)
        print(data)
        return data

# @webhook.hook()        # Defines a handler for the 'push' event
# def on_push(data):  
#     print("Got push with: {0}".format(data))

if __name__ == "__main__":
    app.run()


    # if 'commits' not in data:
    #     # slack inegeration code here will be weritten (not now)
    #     return "not a push event"
    # elif data['action'] == 'opened':        # missing other actions
    #     # slack inegeration code here will be weritten (not now)
    #      return "this is a pull_request"

    # elif data['action'] == 'submitted':     # missing other actions
    #     # slack inegeration code here will be weritten (not now)
    #     return "this is a pull_request_review"

    # elif data['action'] == 'created':       # missing other actions
    #     # slack inegeration code here will be weritten (not now)
    #     return "this is a pull_request_review_comment"






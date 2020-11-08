import os
from flask import Flask
from flask import request, Response
from flask import json
from github_webhook import Webhook
from github import Github
from pathlib import Path
from dotenv import load_dotenv
from slack import WebClient


app = Flask(__name__)
webhook = Webhook(app) # Defines '/postreceive' endpoint

@app.route('/', methods=['GET', 'POST'])
def homepage():
    return "test 999999999999"

# @app.route('/', methods=['GET'])
@app.route('/webhook', methods=['GET','POST'])
def get_github_payload():
    if request.headers['Content-Type'] == 'application/json':
        # data = json.dumps(request.json)
        data = request.json
        webhook_url = 'WEBHOOK_URL'
        slack_data = {"text": "hello world 2020"}
        response = request.post(
            webhook_url, data=json.dumps(slack_data),
            headers={'Content-Type': 'application/json'}


        )
        print(data)
        return data

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)


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






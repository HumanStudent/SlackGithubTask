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

@app.route('/', methods=['GET','POST'])
def homepage():
    return "test hhh"

# @app.route('/', methods=['GET'])
@app.route("/webhook", methods=['GET', 'POST'])
def respond():
    print("** New Payload from GitHub **")
    print(request.json);
    return Response(status=200)

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






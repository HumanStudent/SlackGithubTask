import os
from flask import Flask
from flask import request
from flask import json
from github_webhook import Webhook
from github import Github
from pathlib import Path
from dotenv import load_dotenv
from slack import WebClient

# env_path = Path('.') / '.env'
# load_dotenv(dotenv_path=env_path) 
# gitToken = os.environ['GITTOKEN']
# g = Github(gitToken)
# client = WebClient(token=os.environ['BOB_THE_BOT_TOKEN'])



app = Flask(__name__)
webhook = Webhook(app) # Defines '/postreceive' endpoint

# @app.route('/')
# def homepage():
#     return "test 123456879"

# @app.route('/', methods=['GET'])
# @app.route('/')
# def get_github_payload():
#     data = request.get_json()
#     if 'commits' not in data:
#         # slack inegeration code here will be weritten (not now)
#         return "not a push event"
#     client.chat_postMessage(channel='#testbotbot', text="hello from the other side")

@app.route('/webhook')
def get_github_notafication():
    if request.headers['Content-Type'] == 'application/json':
        data = json.dumps(request.json)
    print(data)
    return data 


    # elif data['action'] == 'opened':        # missing other actions
    #     # slack inegeration code here will be weritten (not now)
    #      return "this is a pull_request"

    # elif data['action'] == 'submitted':     # missing other actions
    #     # slack inegeration code here will be weritten (not now)
    #     return "this is a pull_request_review"

    # elif data['action'] == 'created':       # missing other actions
    #     # slack inegeration code here will be weritten (not now)
    #     return "this is a pull_request_review_comment"
    
    # return data

@webhook.hook()        # Defines a handler for the 'push' event
def on_push(data):
    print("Got push with: {0}".format(data))


if __name__ == "__main__":
    app.run()


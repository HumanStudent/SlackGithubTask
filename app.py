import os
from flask import Flask
from flask import request, Response
from flask import json
from github_webhook import Webhook
from github import Github
from pathlib import Path
from dotenv import load_dotenv
from slack import WebClient

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
client = WebClient(token=os.environ['BOB_THE_BOT_TOKEN'])

def send_to_slack( text_to_send ,channel="#testbotbot"):
    client.chat_postMessage(channel= channel, text=text_to_send)

app = Flask(__name__)
webhook = Webhook(app) # Defines '/postreceive' endpoint

@app.route('/', methods=['GET','POST'])
def homepage():
    return "test hhh"

@app.route("/webhook", methods=['GET', 'POST'])
def respond():
    if request.method == 'GET':
        print("This is a GET request")
    if request.method == 'POST':
        print("AMIGO")
    print("** New Payload from GitHub **")
    data = request.json
    headers = request.headers
    headers_event = request.headers['X-GitHub-Event']
    repo_name = data['repository']['name']
    event_date_time = data['repository']['updated_at']
    print("***************************************************************************")
    print("Headers are: " + str(headers))
    print(headers_event + '   ' +repo_name + '   ' +event_date_time )
    # send_to_slack(headers_event)
    
    return data

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080,debug=True)


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






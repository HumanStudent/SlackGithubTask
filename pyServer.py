import os
from flask import Flask
from flask import request
from flask import json
from github_webhook import Webhook
from github import Github
from pathlib import Path
from dotenv import load_dotenv

# env_path = Path('.') / '.env'
# load_dotenv(dotenv_path=env_path) 
# gitToken = os.environ['GITTOKEN']
# g = Github(gitToken)


app = Flask(__name__)
webhook = Webhook(app) # Defines '/postreceive' endpoint

# @app.route('/')
# def homepage():
#     return "test 123456879"


@app.route('/')
def get_github_notafication():
    if request.headers['Content-Type'] == 'application/json':
        temp_data = json.dumps(request.json, indent=2)
        data = json.dumps(temp_data,indent=2)
        print(data)
        return data

@webhook.hook()        # Defines a handler for the 'push' event
def on_push(data):  
    print("Got push with: {0}".format(data))


if __name__ == "__main__":
    app.run()


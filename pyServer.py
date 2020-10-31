from flask import Flask
from flask import request
from flask import json
from github_webhook import Webhook

# init and creating our flask application
app = Flask(__name__)

@app.route('/')
def homepage():
    return "Hello Its Home"

@app.route('/github', methods=['POST'])
def get_github_notafication():
    if request.headers['Content-Type'] == 'application/json':
        data = json.dumps(request.json)
        print(data)
        return data

# # Defines a handler for the 'push' event
# @webhook.hook()       
# def on_push(data):
#     print("Got push with: {0}".format(data))


if __name__ == '__main__':
    app.run()


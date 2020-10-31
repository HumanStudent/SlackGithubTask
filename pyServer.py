from flask import Flask
from flask import request
from flask import json
from github_webhook import Webhook

# init and creating our flask application
app = Flask(__name__)
webhook = Webhook(app) # Defines '/postreceive' endpoint

@app.route('/')
def homepage():
    return "test 123456879"

@webhook.hook()        # Defines a handler for the 'push' event
def on_push(data):
    print("Got push with: {0}".format(data))

@app.route('/github', methods=['POST'])
def get_github_notafication():
    if request.headers['Content-Type'] == 'application/json':
        data = json.dumps(request.json)
        print(data)
        return data


if __name__ == "__main__":
    app.run()


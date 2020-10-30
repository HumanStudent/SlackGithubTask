import os
from slack import WebClient
from pathlib import Path
from dotenv import load_dotenv
from slack.errors import SlackApiError


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
client = WebClient(token=os.environ['BOB_THE_BOT_TOKEN'])
client.chat_postMessage(channel='#testbotbot', text="hello agian its me")

# try:
#     response = client.chat_postMessage(
#         channel='#test',

#         text="Hello Hello")
#     assert response["message"]["text"] == "Hello world!"
# except SlackApiError as e:
#     # You will get a SlackApiError if "ok" is False
#     assert e.response["ok"] is False
#     assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
#     print(f"Got an error: {e.response['error']}")
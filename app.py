from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

TOKEN = "xoxb-1314932376274-6474310423092-OcbCWkiO8VtCHUarkfTxT6q5";
# instantiate the client 
client = WebClient(token=TOKEN)

def send_message(channel, message):
    try:
        response = client.chat_postMessage(channel=channel, text=message)
        print(response["message"]["text"])
    except SlackApiError as e:
        if e.response["ok"] is False:
            print(f"Got an error: {e.response['error']}")
        if isinstance(e.response.status_code, int):
            print(f"Received a response status_code: {e.response.status_code}")


send_message("#network-team","POD is going to destroy. You 2minute to recover it. I am from dark web.");

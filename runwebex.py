import requests, os

def send_message2Summer(question):
    webex_msg_api_url = 'https://webexapis.com/v1/messages'

    WEBEX_ACCESS_TOKEN = os.getenv("WEBEX_ACCESS_TOKEN")
    ASK_SUMMER_BOT_ID = os.getenv("ASK_SUMMER_BOT_ID")
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {WEBEX_ACCESS_TOKEN}'
    }

    msg = {
        "roomId": ASK_SUMMER_BOT_ID,
        "text": f'{question}'
    }

    requests.post(webex_msg_api_url, headers=headers, json = msg)

    return "I will let Summer know."

send_message2Summer('A question from web')

import requests

from webex import WEBEX_ACCESS_TOKEN, WEBEX_MSG_API_URL, ASK_SUMMER_BOT_ID

def send_message2Summer(question):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {WEBEX_ACCESS_TOKEN}'
    }

    msg = {
        "roomId": ASK_SUMMER_BOT_ID,
        "text": f'{question}'
    }

    res = requests.post(WEBEX_MSG_API_URL, headers=headers, json = msg)

    return res.text
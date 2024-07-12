# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from datetime import datetime, timedelta

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)

def receive_recent_messages_by(date: datetime, from_: str = None, to: str = None):
    messages1 = client.messages.list(
        date_sent_after=date,
        from_=from_,
        # to=to,
    )

    messages2 = client.messages.list(
        date_sent_after=date,
        from_=to,
        # to=to,
    )
    
    messages = messages1 + messages2
    messages = sorted(messages, key=lambda x: x.date_sent)  # Sort by date_sent
    return messages

def receive_recent_7days_messages_by(from_: str = None, to: str = None):
    messages = client.messages.list(
        date_sent_after=datetime.now().date() - timedelta(days=7),
        from_=from_,
        to=to,
    )

    msgs = [{
            'body': message.body,
            'date_sent': message.date_sent,
            'from': message.from_,
            'to': message.to,
        } for message in messages]

    return msgs

if __name__ == "__main__":
    messages = receive_recent_messages_by(date=datetime.now().date() - timedelta(days=7), from_="+18559563669", to="+14088323545")
    for record in messages:
        print(record.sid),
        print(record.body)
        print(record.date_sent)
        print(record.from_)
        print(record.to)
        print("----")
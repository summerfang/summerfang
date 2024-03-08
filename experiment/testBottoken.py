import requests

# Replace with your actual bot access token
bot_access_token = "OGU4NGE2YTItY2UxZC00ODRiLTgzZDAtZWFlYjQ2N2E3Mjc2NzdiZThhMGItNmYy_PF84_505dfc47"

# Replace with the room ID where you want to send the message
room_id = "Y2lzY29zcGFyazovL3VzL1JPT00vNDM3ZDYxMjAtM2U4Yi0xMWVkLWI0YTEtYzVjODQ5YWVmNmUw"

# The message you want to send
message_text = "Hello from my Webex bot! 🤖"

# API endpoint for sending messages
url = "https://api.ciscospark.com/v1/messages"

# Create the payload
payload = {
    "roomId": room_id,
    "text": message_text
}

# Set the authorization header with the bot access token
headers = {
    "Authorization": f"Bearer {bot_access_token}"
}

# Send the POST request to send the message
response = requests.post(url, json=payload, headers=headers)

# Check if the message was sent successfully
if response.status_code == 200:
    print("Message sent successfully!")
else:
    print(f"Error sending message. Status code: {response.status_code}")

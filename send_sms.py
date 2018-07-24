import os
import json
import csv
from twilio.rest import Client

with open('configtwilio.json', 'r') as f:
    config = json.load(f)


# Your Account SID from twilio.com/console
account_sid = config['TEST']['ACCOUNT_SID']
# Your Auth Token from twilio.com/console
auth_token  = config['TEST']['AUTH_TOKEN']

client = Client(account_sid, auth_token)


with open("receivers.csv") as f:
    reader = csv.reader(f)
    receivers = [r for r in reader]


for phone_number in receivers:

    message = client.messages.create(
        to=phone_number,
        from_=config['SENDER'],
        body=config['BODY'])

    print(message.sid)
